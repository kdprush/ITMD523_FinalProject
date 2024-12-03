document.addEventListener("DOMContentLoaded", () => {
    const conversationList = document.getElementById("conversationList");
    const chatMessages = document.getElementById("chatMessages");
    const chatRecipient = document.getElementById("chatRecipient");
    const messageInput = document.getElementById("messageInput");
    const sendMessageButton = document.getElementById("sendMessage");

    let currentRecipient = null;

    // Load Conversations
    async function loadConversations() {
        const response = await fetch("http://127.0.0.1:5000/api/messages/conversations");
        const conversations = await response.json();

        conversationList.innerHTML = ""; // Clear list
        conversations.forEach((conversation) => {
            const li = document.createElement("li");
            li.textContent = conversation.name || conversation.email;
            li.addEventListener("click", () => {
                currentRecipient = conversation.id;
                chatRecipient.textContent = `Chat with ${conversation.name || conversation.email}`;
                loadMessages(conversation.id);
                document.querySelectorAll("#conversationList li").forEach(item => item.classList.remove("active"));
                li.classList.add("active");
            });
            conversationList.appendChild(li);
        });
    }

    // Load Messages
    async function loadMessages(recipientId) {
        const response = await fetch(`http://127.0.0.1:5000/api/messages/${recipientId}`);
        const messages = await response.json();

        chatMessages.innerHTML = ""; // Clear chat
        messages.forEach((message) => {
            const div = document.createElement("div");
            div.className = `message ${message.sender === "me" ? "sent" : "received"}`;
            div.textContent = message.content;
            chatMessages.appendChild(div);
        });

        chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
    }

    // Send Message
    async function sendMessage() {
        const content = messageInput.value.trim();
        if (!content || !currentRecipient) return;

        const response = await fetch("http://127.0.0.1:5000/api/messages", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ recipient: currentRecipient, content }),
        });

        if (response.ok) {
            messageInput.value = ""; // Clear input
            loadMessages(currentRecipient); // Reload chat
        } else {
            alert("Failed to send message.");
        }
    }

    sendMessageButton.addEventListener("click", sendMessage);
    messageInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Load conversations on page load
    loadConversations();
});