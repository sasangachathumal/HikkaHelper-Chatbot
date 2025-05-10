class ChatHistoryManager:
    def __init__(self):
        self.history = {} # session_id: {'messages': [], 'shown_items': {}, 'last_intent': None}

    def add_message(self, session_id, user_message, bot_response):
        if session_id not in self.history:
            self.history[session_id] = {'messages': [], 'shown_items': {}, 'last_intent': None}
        self.history[session_id]['messages'].append({'user': user_message, 'bot': bot_response})

    def get_history(self, session_id):
        return self.history.get(session_id, {'messages': []})['messages']

    def get_last_bot_message(self, session_id):
        history = self.get_history(session_id)
        if history and history[-1]['bot']:
            return history[-1]['bot']
        return None

    def update_shown_item_ids(self, session_id, category, item_ids):
        if session_id not in self.history:
            self.history[session_id] = {'messages': [], 'shown_items': {}, 'last_intent': None}
        if category not in self.history[session_id]['shown_items']:
            self.history[session_id]['shown_items'][category] = []
        self.history[session_id]['shown_items'][category].extend(item_ids)
        self.history[session_id]['shown_items'][category] = list(set(self.history[session_id]['shown_items'][category])) # Ensure uniqueness

    def get_shown_item_ids(self, session_id, category):
        if session_id in self.history and category in self.history[session_id]['shown_items']:
            return self.history[session_id]['shown_items'][category]
        return []

    def set_last_intent(self, session_id, intent):
        if session_id not in self.history:
            self.history[session_id] = {'messages': [], 'shown_items': {}, 'last_intent': None}
        self.history[session_id]['last_intent'] = intent

    def get_last_intent(self, session_id):
        if session_id in self.history:
            return self.history[session_id]['last_intent']
        return None

    def reset_shown_item_ids(self, session_id, category):
        if session_id in self.history and category in self.history[session_id]['shown_items']:
            self.history[session_id]['shown_items'][category] = []