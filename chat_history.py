# travel_chatbot/chat_history.py

from collections import defaultdict, deque

MAX_HISTORY_LEN = 5 # Keep last 5 turns per session

class ChatHistoryManager:
    def __init__(self):
        # Use defaultdict to easily handle new sessions
        # Use deque for efficient appending and limiting history size
        self.histories = defaultdict(lambda: deque(maxlen=MAX_HISTORY_LEN))

    def add_message(self, session_id, user_msg, bot_msg):
        """Adds a user message and bot response to the session history."""
        if not session_id: # Handle cases without specific session management
             session_id = "default_session"
        self.histories[session_id].append({"user": user_msg, "bot": bot_msg})

    def get_history(self, session_id):
        """Retrieves the chat history for a given session."""
        if not session_id:
             session_id = "default_session"
        return list(self.histories[session_id]) # Return as a list

    def get_last_bot_message(self, session_id):
        """Gets the last message sent by the bot in the session."""
        if not session_id:
             session_id = "default_session"
        history = self.histories[session_id]
        if history:
            return history[-1].get("bot")
        return None

    # --- Potential Enhancements for using history ---
    # def get_context_keywords(self, session_id):
    #     """Extract keywords from recent conversation for context."""
    #     history = self.get_history(session_id)
    #     # Implement logic to extract relevant nouns/keywords from recent turns
    #     # e.g., using POS tagging or simple frequency analysis
    #     keywords = set()
    #     if history:
    #         last_turn = history[-1]
    #         # Simple: add words from last user message (needs better NLP)
    #         keywords.update(last_turn['user'].lower().split())
    #     return list(keywords)