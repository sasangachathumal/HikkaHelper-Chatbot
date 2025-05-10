import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import TextPreprocessor

INTENTS_PATH = 'intents.json'
MODEL_PATH = 'chatbot_model.pkl'

def train():
    """Trains the TF-IDF model based on intents.json and saves it."""
    print("Starting model training...")
    try:
        with open(INTENTS_PATH, 'r') as f:
            intents_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INTENTS_PATH} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {INTENTS_PATH}.")
        return

    patterns = []
    tags = []
    preprocessor = TextPreprocessor()

    for intent in intents_data['intents']:
        for pattern in intent['patterns']:
            processed_pattern = preprocessor.preprocess(pattern)
            patterns.append(processed_pattern)
            tags.append(intent['tag'])

    if not patterns:
        print("No patterns found in intents file. Training aborted.")
        return

    # Initialize and train TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    intent_vectors = vectorizer.fit_transform(patterns)

    # Prepare data to save
    model_data = {
        'vectorizer': vectorizer,
        'intent_vectors': intent_vectors,
        'tags': tags # Store the tag corresponding to each vector row
    }

    # Save the model using joblib
    try:
        joblib.dump(model_data, MODEL_PATH)
        print(f"Model trained and saved successfully to {MODEL_PATH}")
    except Exception as e:
        print(f"Error saving model: {e}")

if __name__ == '__main__':
    train()