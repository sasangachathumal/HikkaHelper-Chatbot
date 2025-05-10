(function() {
    let chatWidget = null;
    let chatButton = null;
    let chatContainer = null;
    let userInput = null;
    let sendButton = null;
    let sessionId = null;
    const apiUrl = '/chat';

    function createChatWidget() {
        chatWidget = document.createElement('div');
        chatWidget.id = 'hikka-helper-widget';
        chatWidget.style.position = 'fixed';
        chatWidget.style.bottom = '20px';
        chatWidget.style.right = '20px';
        chatWidget.style.zIndex = '1000';
        chatWidget.style.display = 'none';
        chatWidget.style.border = '1px solid #ccc';
        chatWidget.style.borderRadius = '5px';
        chatWidget.style.backgroundColor = '#f9f9f9';
        chatWidget.style.width = '300px';
        chatWidget.style.height = '400px';
        chatWidget.style.flexDirection = 'column';
        chatWidget.style.display = 'flex';

        chatContainer = document.createElement('div');
        chatContainer.id = 'hikka-chat-container';
        chatContainer.style.flexGrow = '1';
        chatContainer.style.overflowY = 'scroll';
        chatContainer.style.padding = '10px';

        const inputArea = document.createElement('div');
        inputArea.style.padding = '10px';
        inputArea.style.borderTop = '1px solid #eee';
        inputArea.style.display = 'flex';

        userInput = document.createElement('input');
        userInput.type = 'text';
        userInput.placeholder = 'Type your message...';
        userInput.style.flexGrow = '1';
        userInput.style.padding = '8px';
        userInput.style.marginRight = '5px';
        userInput.style.borderRadius = '3px';
        userInput.style.border = '1px solid #ddd';

        sendButton = document.createElement('button');
        sendButton.textContent = 'Send';
        sendButton.style.padding = '8px 15px';
        sendButton.style.borderRadius = '3px';
        sendButton.style.backgroundColor = '#007bff';
        sendButton.style.color = 'white';
        sendButton.style.border = 'none';
        sendButton.style.cursor = 'pointer';

        inputArea.appendChild(userInput);
        inputArea.appendChild(sendButton);

        chatWidget.appendChild(chatContainer);
        chatWidget.appendChild(inputArea);

        document.body.appendChild(chatWidget);

        sendButton.addEventListener('click', sendMessage);
        userInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                sendMessage();
            }
        });
    }

    function createChatButton() {
        chatButton = document.createElement('button');
        chatButton.id = 'hikka-helper-button';
        chatButton.textContent = 'Chat with HikkaHelper';
        chatButton.style.position = 'fixed';
        chatButton.style.bottom = '20px';
        chatButton.style.right = '20px';
        chatButton.style.zIndex = '1001';
        chatButton.style.padding = '10px 20px';
        chatButton.style.backgroundColor = '#007bff';
        chatButton.style.color = 'white';
        chatButton.style.border = 'none';
        chatButton.style.borderRadius = '5px';
        chatButton.style.cursor = 'pointer';

        document.body.appendChild(chatButton);

        chatButton.addEventListener('click', () => {
            chatWidget.style.display = 'flex';
            chatButton.style.display = 'none';
        });
        createChatWidget();
    }

    function addMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(`hikka-${sender}-message`);
        messageDiv.textContent = message;
        messageDiv.style.textAlign = sender === 'user' ? 'right' : 'left';
        messageDiv.style.color = sender === 'user' ? 'blue' : 'green';
        messageDiv.style.marginBottom = '5px';
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessage('user', message);
            userInput.value = '';

            fetch(apiUrl, {
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
                    sessionId = data.session_id;
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
    createChatButton();
})();