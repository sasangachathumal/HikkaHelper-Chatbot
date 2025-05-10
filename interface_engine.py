import random
import json
from nlp_service import NLProcessor
from database import get_info_by_category, log_interaction, get_total_item_count_by_category
from chat_history import ChatHistoryManager

INTENTS_PATH = 'intents.json'
# Minimum confidence score to accept an intent match
CONFIDENCE_THRESHOLD = 0.6

class InferenceEngine:
    def __init__(self):
        self.nlp = NLProcessor()
        self.history_manager = ChatHistoryManager()
        self.intents = self._load_intents()
        self.intent_responses = self._map_intent_responses()

    def _load_intents(self):
        """Loads intent definitions from the JSON file."""
        try:
            with open(INTENTS_PATH, 'r') as f:
                return json.load(f)['intents']
        except Exception as e:
            print(f"Error loading intents file: {e}")
            return [] # Return empty list on error

    def _map_intent_responses(self):
        """Creates a dictionary mapping intent tags to their response lists."""
        response_map = {}
        for intent in self.intents:
            response_map[intent['tag']] = intent['responses']
        return response_map

    def _get_total_item_count(self, category):
        """Gets the total number of items for a category from the database."""
        if category:
            return get_total_item_count_by_category(category)
        return 0

    def _get_random_response(self, tag):
        """Selects a random response for a given intent tag."""
        if tag in self.intent_responses and self.intent_responses[tag]:
            return random.choice(self.intent_responses[tag])
        return "Sorry, I seem to be missing a response for that." # Fallback

    def _handle_knowledge_query(self, tag, session_id):
        """Handles intents that require database lookups with session awareness."""
        category_map = {
            'find_hotels': 'hotel',
            'find_activities': 'activity',
            'weather_query': 'weather',
            'location_info': 'general_info',
            'getting_around': 'getting_around',
            'local_food': 'local_food',
            'surfing_spots': 'surfing_spots',
            'snorkeling_diving': 'snorkeling_diving',
            'budget_travel': 'budget_travel',
            'safety_tips': 'safety_tips'
        }
        category = category_map.get(tag)
        if category:
            initial_response = self._get_random_response(tag)
            shown_ids = self.history_manager.get_shown_item_ids(session_id, category)
            total_item_count = self._get_total_item_count(category=category)
            # Number of results to fetch per turn
            limit = 3

            if shown_ids and len(shown_ids) >= total_item_count:
                # All items have been shown, reset the shown IDs to start over
                self.history_manager.reset_shown_item_ids(session_id, category)
                shown_ids = []  # Reset the local shown_ids for the current query

            db_results_data = get_info_by_category(category, limit=limit, exclude_ids=shown_ids)

            if db_results_data and db_results_data['results']:
                formatted_response = f"{initial_response}\n\n"
                for item in db_results_data['results']:
                    name = item.get('name')
                    description = item.get('description')
                    details_str = item.get('details')
                    details = json.loads(details_str) if details_str else {}

                    if name:
                        formatted_response += f"**{name}**\n"
                    if description:
                        formatted_response += f"- {description}\n"
                    if details:
                        for key, value in details.items():
                            formatted_response += f"  - {key.replace('_', ' ').title()}: {value}\n"
                    formatted_response += "\n"

                self.history_manager.update_shown_item_ids(session_id, category, db_results_data['ids'])
                return formatted_response.strip()
            else:
                return f"Sorry, I don't have any more information about {category.replace('_', ' ')} right now."
        else:
            return self._get_random_response(tag)

    def get_response(self, user_input, session_id=None):
        """
        Processes user input, predicts intent, fetches response/data, and manages history with context.
        """
        bot_response = "Sorry, I didn't quite understand that. Can you please rephrase?"  # Default fallback
        predicted_tag = None
        confidence = 0.0

        if self.nlp.vectorizer:
            predicted_tag, confidence = self.nlp.predict_intent(user_input)
            print(f"Input: '{user_input}' -> Predicted Intent: {predicted_tag}, Confidence: {confidence:.2f}")

            if confidence >= CONFIDENCE_THRESHOLD:
                if predicted_tag.startswith(('find_', 'query_', 'weather_', 'location_', 'getting_', 'local_', 'surfing_', 'snorkeling_', 'budget_', 'safety_')):
                    bot_response = self._handle_knowledge_query(predicted_tag, session_id)
                    self.history_manager.set_last_intent(session_id, predicted_tag)  # Store last knowledge-based intent
                elif predicted_tag in self.intent_responses:
                    bot_response = self._get_random_response(predicted_tag)
                    self.history_manager.set_last_intent(session_id, predicted_tag)  # Store last intent
                elif "give me other" in user_input.lower() or "show me more" in user_input.lower():
                    last_intent = self.history_manager.get_last_intent(session_id)
                    if last_intent and last_intent.startswith(('find_', 'query_', 'weather_', 'location_', 'getting_', 'local_', 'surfing_', 'snorkeling_', 'budget_', 'safety_')):
                        bot_response = self._handle_knowledge_query(last_intent, session_id)
                    else:
                        bot_response = "Could you please clarify what you'd like to see more of?"
                else:
                    print(f"Warning: High confidence match for unknown tag '{predicted_tag}'. Check intents.json.")
            else:
                print(f"Low confidence match ({confidence:.2f} < {CONFIDENCE_THRESHOLD}). Logging interaction.")
        else:
            bot_response = "Sorry, my NLP brain isn't working right now. Please try again later."

        log_interaction(user_input, predicted_tag, confidence, bot_response)
        self.history_manager.add_message(session_id, user_input, bot_response)

        return bot_response