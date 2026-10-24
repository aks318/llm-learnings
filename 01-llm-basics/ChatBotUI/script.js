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

    // Send message to backend API
    async function sendToBackend(message) {
        try {
            const response = await fetch('http://127.0.0.1:8000/user_prompt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_prompt: message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Handle streaming response
            if (response.headers.get('content-type')?.includes('text/event-stream')) {
                const reader = response.body.getReader();
                const decoder = new TextDecoder();
                
                let fullResponse = "";
                let firstChunk = true;
                
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;
                    
                    const chunk = decoder.decode(value);
                    const lines = chunk.split('\n');
                    
                    for (const line of lines) {
                        if (line.trim() === '') continue;
                        
                        try {
                            const data = JSON.parse(line);
                            if (data.content) {
                                // For streaming, we'll append to the current message
                                fullResponse += data.content;
                                
                                // Update the UI with partial response
                                if (firstChunk) {
                                    // Create new assistant message element if this is first chunk
                                    addAssistantMessage(fullResponse);
                                    firstChunk = false;
                                } else {
                                    // Update existing message with accumulated content
                                    const messages = document.querySelectorAll('.assistant-message');
                                    if (messages.length > 0) {
                                        const lastMessage = messages[messages.length - 1];
                                        lastMessage.textContent = fullResponse;
                                    }
                                }
                            }
                        } catch (e) {
                            console.error('Error parsing stream:', e);
                        }
                    }
                }
                
                return { content: fullResponse };
            } else {
                // Handle non-streaming response (fallback)
                const data = await response.json();
                return data;
            }
        } catch (error) {
            console.error('Error sending to backend:', error);
            throw error;
        }
    }

    // Generate assistant response by calling backend
    async function generateAssistantResponse() {
        try {
            // Get the last user message from chat history
            const lastUserMessage = chatHistory[chatHistory.length - 1]?.content || "";
            
            // Send to backend and get response
            const result = await sendToBackend(lastUserMessage);
            
            // Add the assistant response to UI (this will be called if not streaming)
            if (!result.content) {
                addAssistantMessage("No content received from AI service.");
            }
        } catch (error) {
            console.error('Error in generateAssistantResponse:', error);
            // Fallback to static response if backend fails
            const fallbackResponses = [
                "I apologize, but I'm currently having trouble connecting to the backend service. Here's a general response based on similar queries...",
                "There seems to be an issue with the connection to the AI service. In the meantime, here's what I can tell you about this topic...",
                "The system is experiencing temporary difficulties. However, based on my knowledge, I can provide some general insights on your question."
            ];
            
            const fallbackResponse = fallbackResponses[Math.floor(Math.random() * fallbackResponses.length)];
            addAssistantMessage(fallbackResponse);
        }
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