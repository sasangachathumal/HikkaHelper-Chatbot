import joblib
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
from utils import TextPreprocessor

MODEL_PATH = 'chatbot_model.pkl'
INTENTS_PATH = 'intents.json'

class NLProcessor:
    def __init__(self):
        self.vectorizer = None
        self.intent_vectors = None
        self.tags = None
        self.preprocessor = TextPreprocessor()
        self._load_model()

    def _preprocess(self, text):
        return self.preprocessor.preprocess(text)

    def _load_model(self):
        """Loads the trained TF-IDF vectorizer and intent vectors."""
        if os.path.exists(MODEL_PATH):
            try:
                model_data = joblib.load(MODEL_PATH)
                self.vectorizer = model_data['vectorizer']
                self.intent_vectors = model_data['intent_vectors']
                self.tags = model_data['tags']
                print("NLP Model loaded successfully.")
            except Exception as e:
                print(f"Error loading model: {e}. Please retrain the model.")
                self.vectorizer = None
        else:
            print(f"Model file ({MODEL_PATH}) not found. Please train the model first.")

    def predict_intent(self, text):
        """Predicts the intent of the user input using TF-IDF and Cosine Similarity."""
        if not self.vectorizer or self.intent_vectors is None or self.tags is None:
            print("NLP model not loaded. Cannot predict intent.")
            # Return None intent and 0 confidence
            return None, 0.0

        processed_text = self._preprocess(text)
        text_vector = self.vectorizer.transform([processed_text])
        print(f"processed_text - {processed_text}")

        # Calculate cosine similarities
        similarities = cosine_similarity(text_vector, self.intent_vectors)
        print(f"similarities - {similarities}")

        # Find the best match
        best_match_index = np.argmax(similarities)
        confidence = similarities[0, best_match_index]
        predicted_tag = self.tags[best_match_index]

        return predicted_tag, float(confidence)