# travel_chatbot/seed_data.py

from database import init_db, add_knowledge, get_db_connection

def seed():
    """Populates the database with initial Hikkaduwa information."""
    print("Seeding database...")
    init_db() # Ensure tables exist

    # Clear existing data for idempotency (optional)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM knowledge")
    conn.commit()
    conn.close()

    # Add Sample Data
    add_knowledge(
        category='hotel',
        name='Hikka Tranz by Cinnamon',
        description='Popular beachfront hotel with vibrant atmosphere and amenities.',
        details='Address: Galle Rd, Hikkaduwa. Features: Pool, Restaurants, Bar, Beach Access.',
        relevance=5
    )
    add_knowledge(
        category='hotel',
        name='Citrus Hikkaduwa',
        description='Modern hotel offering sea views and comfortable rooms.',
        details='Address: Galle Rd, Hikkaduwa. Features: Pool, Restaurant, Spa.',
        relevance=5
    )
    add_knowledge(
        category='hotel',
        name='Riff Hikkaduwa',
        description='Luxury boutique hotel known for its design and service.',
        details='Address: Narigama, Hikkaduwa. Features: Infinity Pool, Fine Dining, Beachfront.',
        relevance=3
    )
    add_knowledge(
        category='activity',
        name='Surfing',
        description='Hikkaduwa is famous for surfing, with spots suitable for beginners and experienced surfers.',
        details='Best Season: November to April. Main surf points near the main beach and Narigama.'
    )
    add_knowledge(
        category='activity',
        name='Snorkeling & Diving',
        description='Explore the coral reefs and marine life at the Hikkaduwa Coral Sanctuary.',
        details='Equipment rentals available near the beach. Glass bottom boat tours are also popular.'
    )
    add_knowledge(
        category='activity',
        name='Turtle Hatchery Visit',
        description='Visit nearby turtle hatcheries to learn about conservation efforts and see turtles.',
        details='Several hatcheries located a short drive from Hikkaduwa.'
    )
    add_knowledge(
        category='weather',
        description='Hikkaduwa has a tropical climate. The main tourist season (dry) is typically from November to April. The monsoon season is usually May to October, but showers can occur anytime.',
        details=f'Today is {datetime.now().strftime("%Y-%m-%d")}. For a current forecast, please check a reliable weather website.' # Dynamic part would need live data
    )
    add_knowledge(
        category='general_info',
        description='Hikkaduwa is a coastal town in southwestern Sri Lanka, known for its beaches, coral reefs, and nightlife.',
        details='Located about 100km south of Colombo.'
    )

    print("Database seeding complete.")

if __name__ == '__main__':
    from datetime import datetime # Import here for the seeding script
    seed()