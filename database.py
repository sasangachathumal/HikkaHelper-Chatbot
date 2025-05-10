import sqlite3
import os

DATABASE_DIR = 'data'
DATABASE_PATH = os.path.join(DATABASE_DIR, 'hikkahelper_kb.db')

def init_db():
    """Initializes the database and creates tables if they don't exist."""
    if not os.path.exists(DATABASE_DIR):
        os.makedirs(DATABASE_DIR)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # Using a single 'knowledge' table for simplicity
    # category examples: 'hotel', 'activity', 'restaurant', 'general_info', 'weather'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            name TEXT,
            description TEXT NOT NULL,
            details TEXT,
            relevance INTEGER DEFAULT 0
        )
    ''')
    # Table for logging user interactions for learning
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learning_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            user_input TEXT NOT NULL,
            predicted_intent TEXT,
            confidence REAL,
            bot_response TEXT,
            feedback TEXT -- Could be used for explicit feedback later
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized.")

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row # Return rows as dictionary-like objects
    return conn

def add_knowledge(category, description, name=None, details=None, relevance=0):
    """Adds a piece of knowledge to the database with optional relevance."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO knowledge (category, name, description, details, relevance) VALUES (?, ?, ?, ?, ?)",
        (category.lower(), name, description, details, relevance)
    )
    conn.commit()
    conn.close()

def get_total_item_count_by_category(category):
    """Retrieves the total number of items for a given category."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM knowledge WHERE category = ?", (category.lower(),))
    result = cursor.fetchone()
    count = result[0] if result else 0  # Access the first element of the tuple
    conn.close()
    return count

def get_info_by_category(category, limit=None, offset=None, exclude_ids=None):
    """Retrieves information based on the category with optional limit, offset, and exclusion, ordered by relevance."""
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT id, name, description, details FROM knowledge WHERE category = ?"
    params = [category.lower()]
    if exclude_ids:
        sql += " AND id NOT IN ({})".format(','.join('?' * len(exclude_ids)))
        params.extend(exclude_ids)
    sql += " ORDER BY relevance DESC"  # Order by relevance (highest first)
    if limit is not None:
        sql += " LIMIT ?"
        params.append(limit)
    if offset is not None:
        sql += " OFFSET ?"
        params.append(offset)

    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()

    if not results:
        return f"Sorry, I don't have specific information about {category} in Hikkaduwa right now."

    item_ids = [row['id'] for row in results]
    return {"results": [dict(row) for row in results], "ids": item_ids}

def log_interaction(user_input, predicted_intent, confidence, bot_response):
    """Logs an interaction for potential learning/review."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO learning_log (user_input, predicted_intent, confidence, bot_response) VALUES (?, ?, ?, ?)",
        (user_input, predicted_intent, confidence, bot_response)
    )
    conn.commit()
    conn.close()
