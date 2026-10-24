document.addEventListener('DOMContentLoaded', () => {
    // DOM elements
    const chatContainer = document.getElementById('chat-container');
    const messagesContainer = document.getElementById('messages');
    const messageInput = document.getElementById('message-input');
    const sendBtn = document.getElementById('send-btn');
    const newChatBtn = document.getElementById('new-chat-btn');
    const clearChatBtn = document.getElementById('clear-chat-btn');
    const welcomeScreen = document.getElementById('welcome-screen');
    const typingIndicator = document.getElementById('typing-indicator');
    const promptBtns = document.querySelectorAll('.prompt-btn');

    // Initialize chat state
    let chatHistory = [];

    // Auto-resize textarea
    messageInput.addEventListener('input', () => {
        messageInput.style.height = 'auto';
        messageInput.style.height = (messageInput.scrollHeight) + 'px';
    });

    // Handle sending messages
    function sendMessage() {
        const message = messageInput.value.trim();
        
        if (!message) return;

        // Add user message to UI
        addUserMessage(message);
        chatHistory.push({ role: 'user', content: message });
        
        // Clear input and hide welcome screen
        messageInput.value = '';
        messageInput.style.height = 'auto';
        welcomeScreen.style.display = 'none';

        // Show typing indicator
        typingIndicator.style.display = 'block';
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        // Generate assistant response after a delay
        setTimeout(() => {
            generateAssistantResponse();
        }, 1000);
    }

    // Add user message to UI
    function addUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'user-message');
        messageElement.textContent = message;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    // Add assistant message to UI
    function addAssistantMessage(message) {
        typingIndicator.style.display = 'none';
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'assistant-message');
        messageElement.textContent = message;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    // Generate a mock assistant response
    function generateAssistantResponse() {
        const responses = [
            "That's an interesting question! Let me think about how to best explain that to you. I'll provide a comprehensive answer with plenty of detail.",
            "Thanks for your message. I'm here to help with whatever you need assistance on. Let me break this down for you in a clear and structured way.",
            "I understand what you're asking. Here's my perspective on that topic: This is an important subject with several key aspects to consider.",
            "Great question! Based on my knowledge, here's what I can tell you... This is a multifaceted issue that deserves thorough examination.",
            "I've processed your request and here's a detailed answer: The core concepts involved are quite fascinating and intricate.",
            "That's a thoughtful inquiry. Here's my analysis on this subject: There are several important considerations we should explore together.",
            "I appreciate you reaching out about this. Let me provide some insights with additional context and explanation to help you understand better."
        ];
        
        const randomResponse = responses[Math.floor(Math.random() * responses.length)];
        
        // Add more padding/complexity to the response
        let fullResponse = randomResponse;
        if (Math.random() > 0.5) {
            fullResponse += " The explanation involves multiple dimensions that I'll elaborate on in detail. This subject has various interconnected elements that contribute to a complete understanding.";
        }
        
        addAssistantMessage(fullResponse);
    }

    // Event listeners for sending messages
    sendBtn.addEventListener('click', sendMessage);

    messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // New chat button
    newChatBtn.addEventListener('click', () => {
        // Clear messages and history
        messagesContainer.innerHTML = '';
        chatHistory = [];
        
        // Show welcome screen again
        welcomeScreen.style.display = 'flex';
    });

    // Clear chat button
    clearChatBtn.addEventListener('click', () => {
        messagesContainer.innerHTML = '';
        chatHistory = [];
        welcomeScreen.style.display = 'flex';
    });

    // Suggested prompts
    promptBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            messageInput.value = btn.getAttribute('data-prompt');
            sendMessage();
        });
    });
});