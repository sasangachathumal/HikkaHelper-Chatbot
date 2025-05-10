from flask import Flask, request, jsonify, render_template, send_from_directory, session
from interface_engine import InferenceEngine
import os
# For basic session management
import uuid
from database import init_db, log_interaction

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.static_folder = 'static'
app.template_folder = 'templates'

# Initialize the Inference Engine (loads NLP model, intents)
inference_engine = InferenceEngine()

@app.route('/')
def index():
    """Serves the main HTML page for the chatbot."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handles incoming chat messages."""
    try:
        data = request.get_json()
        user_message = request.json.get('message')
        session_id = request.json.get('session_id')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Basic session ID generation if not provided
        if not session_id:
            session_id = str(uuid.uuid4())

        # Get response from the inference engine
        bot_reply = inference_engine.get_response(user_message, session_id=session_id)

        return jsonify({'reply': bot_reply, 'session_id': session_id})

    except Exception as e:
        print(f"Error in /chat endpoint: {e}")
        return jsonify({'error': 'An internal error occurred'}), 500

@app.route('/hikkaHelper.js')
def chat_js():
    """Serves the embeddable JavaScript file."""
    return send_from_directory(app.static_folder, 'hikkaHelper.js')

# Optional: Route to trigger retraining (for development/admin)
@app.route('/retrain', methods=['POST'])
def retrain_model():
    try:
        from train_model import train
        train()
        # Re-initialize the inference engine to load the new model
        global inference_engine
        inference_engine = InferenceEngine()
        return jsonify({'status': 'Model retraining initiated and reloaded.'})
    except Exception as e:
        print(f"Error during retraining: {e}")
        return jsonify({'error': f'Retraining failed: {e}'}), 500


if __name__ == '__main__':
    # Ensure database exists before starting (run seed_data.py once)
    if not os.path.exists(os.path.join('data', 'hikkahelper_kb.db')):
         print("Database not found. Please run 'python seed_data.py' first.")
    else:
        # Check if model exists, prompt training if not
        if not os.path.exists('chatbot_model.pkl'):
            print("Chatbot model not found. Please run 'python train_model.py' first.")
        else:
            # Host on 0.0.0.0 to make it accessible on the network
            app.run(host='0.0.0.0', port=5000, debug=True)