document.addEventListener('DOMContentLoaded', () => {
    const chatDisplay = document.getElementById('chat-display');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    let sessionId = localStorage.getItem('sessionId');
    if (!sessionId) {
        sessionId = generateSessionId();
        localStorage.setItem('sessionId', sessionId);
    }

    console.log('Session ID:', sessionId); // For debugging

    function generateSessionId() {
        return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    }

    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        const formattedMessage = marked.parse(message);
        messageDiv.innerHTML = formattedMessage;
        chatDisplay.appendChild(messageDiv);
        chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom
    }

    sendButton.addEventListener('click', () => {
        const message = userInput.value.trim();
        if (message) {
            appendMessage('user', message);
            userInput.value = '';
            sendMessage(message, sessionId);
        }
    });

    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter' && userInput.value.trim()) {
            sendButton.click();
        }
    });

    function sendMessage(message, sessionId) {
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
                    appendMessage('bot', data.reply);
                    sessionId = data.session_id; // Update session ID if received
                } else if (data.error) {
                    appendMessage('bot', `Error: ${data.error}`);
                }
            })
            .catch(error => {
                appendMessage('bot', 'Error: Could not connect to the chatbot.');
                console.error('Error:', error);
            });
    }
});