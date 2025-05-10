# travel_chatbot/inference_engine.py

import random
import json
from nlp_service import NLProcessor
from database import get_info_by_category, log_interaction
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

    def _get_random_response(self, tag):
        """Selects a random response for a given intent tag."""
        if tag in self.intent_responses and self.intent_responses[tag]:
            return random.choice(self.intent_responses[tag])
        return "Sorry, I seem to be missing a response for that." # Fallback

    def _handle_knowledge_query(self, tag):
        """Handles intents that require database lookups."""
        # Map intent tags to database categories
        category_map = {
            'find_hotels': 'hotel',
            'find_activities': 'activity',
            'weather_query': 'weather',
            'location_info': 'general_info'
            # Add mappings for other knowledge-based intents
        }
        category = category_map.get(tag)
        if category:
            # Get initial response (e.g., "Looking up hotels...")
            initial_response = self._get_random_response(tag)
            # Fetch data from DB
            db_results = get_info_by_category(category)
            # Combine initial response with DB results
            return f"{initial_response}\n{db_results}"
        else:
            # If tag is known but not mapped to a DB category (shouldn't happen with good design)
            return self._get_random_response(tag) # Fallback to standard response

    def get_response(self, user_input, session_id=None):
        """
        Processes user input, predicts intent, fetches response/data, and manages history.
        """
        bot_response = "Sorry, I didn't quite understand that. Can you please rephrase?" # Default fallback
        predicted_tag = None
        confidence = 0.0

        if self.nlp.vectorizer: # Check if NLP model is loaded
            predicted_tag, confidence = self.nlp.predict_intent(user_input)

            print(f"Input: '{user_input}' -> Predicted Intent: {predicted_tag}, Confidence: {confidence:.2f}") # Debugging

            if confidence >= CONFIDENCE_THRESHOLD:
                # Check if it's a knowledge query intent
                if predicted_tag.startswith(('find_', 'query_', 'weather_', 'location_')): # Define prefix convention
                    bot_response = self._handle_knowledge_query(predicted_tag)
                # Otherwise, it's a standard conversational intent
                elif predicted_tag in self.intent_responses:
                    bot_response = self._get_random_response(predicted_tag)
                else:
                     # Confidence high, but tag not in responses? Should not happen if intents.json is consistent
                     print(f"Warning: High confidence match for unknown tag '{predicted_tag}'. Check intents.json.")
                     # Keep default fallback response
            else:
                # Low confidence - log for potential learning
                print(f"Low confidence match ({confidence:.2f} < {CONFIDENCE_THRESHOLD}). Logging interaction.")
                # Keep default fallback response. Logging happens below.

        else:
            # NLP Model not loaded scenario
            bot_response = "Sorry, my NLP brain isn't working right now. Please try again later."

        # Log the interaction (especially useful for low confidence or errors)
        log_interaction(user_input, predicted_tag, confidence, bot_response)

        # Add to chat history
        self.history_manager.add_message(session_id, user_input, bot_response)

        # --- Placeholder for using history ---
        # You could potentially modify the response based on history here.
        # Example: If the last bot message was asking a clarifying question,
        # the logic here might interpret the user_input as the answer.
        # This requires more complex state management and NLP.
        # last_bot_msg = self.history_manager.get_last_bot_message(session_id)
        # if last_bot_msg and "Did you mean X or Y?" in last_bot_msg:
             # Process user_input as clarification...

        return bot_response