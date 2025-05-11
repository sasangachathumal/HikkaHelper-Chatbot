# 🌴 HikkaHelper - Your Hikkaduwa Travel Assistant 🏄‍♀️🐢

## 🌊 Project Description

HikkaHelper is a friendly and informative chatbot designed to assist users with their travel plans and queries related to the beautiful coastal town of Hikkaduwa, located in the Southern Province of Sri Lanka. Whether you're looking for the best surfing spots, comfortable hotels, exciting activities, delicious local food, or just need some general information about the area, HikkaHelper is here to guide you!

## ✨ Key Features

* **Intent Recognition:** Understands user queries related to various aspects of Hikkaduwa travel.
* **Knowledge Base:** Stores and retrieves information about hotels 🏨, activities 🏖️, local cuisine 🍜, surfing spots 🏄, weather ☀️, and general information ℹ️ about Hikkaduwa.
* **Contextual Awareness:** Remembers the conversation history to provide more relevant answers to follow-up questions, like suggesting more options for hotels or activities.
* **Formatted Responses:** Presents information in a clear and readable format using Markdown.
* **Easy Setup:** Provides simple scripts for local project setup on different operating systems.

## ⚙️ Technologies Used

* **Natural Language Processing (NLP):**
    * **`nltk` (Natural Language Toolkit):** Used for text processing tasks like tokenization and stemming (initially).
    * **`scikit-learn`:** Employed for creating the TF-IDF vectorizer and training the machine learning model for intent classification.
* **Inference Engine:** Custom Python logic (`interface_engine.py`) to interpret user intents, fetch relevant data, and generate appropriate responses.
* **Database:**
    * **SQLite:** A lightweight, file-based database (`travel_info.db`) to store information about Hikkaduwa.
* **Backend:**
    * **Flask:** A micro web framework in Python (`app.py`) to handle user requests via a web API.
* **Frontend:**
    * **HTML (`templates/index.html`):** Structures the user interface for the chat.
    * **CSS (`static/index.css`):** Styles the visual appearance of the chat UI with a cool green color scheme.
    * **JavaScript (`static/index.js`):** Handles user interactions, sends messages to the backend, and dynamically updates the chat display using the **Marked** library for Markdown rendering.
* **Chat History Management:** Custom Python logic (`chat_history.py`) to maintain conversation context per user session.
* **Setup Scripts:**
    * **Bash (`setup.sh`):** For macOS and Linux environments.
    * **Batch (`setup.bat`):** For Windows environments.

## 🚀 Local Setup and Run

Follow these steps to set up and run HikkaHelper on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone git@github.com:sasangachathumal/HikkaHelper-Chatbot.git
    cd HikkaHelper-Chatbot
    ```

2.  **Run the Setup Script:**
    Execute the appropriate script for your operating system:

    * **macOS/Linux:**
        ```bash
        chmod +x setup.sh
        ./setup.sh
        ```

    * **Windows:**
        Open Command Prompt as Administrator and run:
        ```batch
        setup.bat
        ```
    This script will:
    * Install the necessary Python dependencies from `requirements.txt`.
    * Execute `seed_data.py` to initialize the `travel_info.db` with initial data.

3.  **Run the Flask Application:**
    Navigate to the project directory in your terminal and run the Flask application:
    ```bash
    python app.py
    ```
    (Make sure your virtual environment is activated if you used one during setup).

4.  **Open in your Browser:**
    Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in your terminal when Flask starts). You should see the HikkaHelper chat interface.

5.  **Start Chatting!**
    Type your questions about Hikkaduwa in the input field and press "Send" to interact with HikkaHelper.

Enjoy exploring Hikkaduwa with your personal chat assistant! 🌴🌊🐢🍜🏄☀️