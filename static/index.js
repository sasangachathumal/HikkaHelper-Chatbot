document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-display');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    let sessionId = null; // To store the session ID

    function addMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(`message`);
        messageDiv.classList.add(`${sender}-message`);
        messageDiv.textContent = message;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to bottom
    }

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessage('user', message);
            userInput.value = '';

            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message, session_id: sessionId }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.reply) {
                    addMessage('bot', data.reply);
                    sessionId = data.session_id; // Update session ID if received
                } else if (data.error) {
                    addMessage('bot', `Error: ${data.error}`);
                }
            })
            .catch(error => {
                addMessage('bot', 'Error: Could not connect to the chatbot.');
                console.error('Error:', error);
            });
        }
    }
});