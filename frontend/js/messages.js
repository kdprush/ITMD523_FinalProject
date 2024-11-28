// messages.js: Handles Messaging Functionality

// Load Messages
async function loadMessages() {
    const response = await fetch("http://127.0.0.1:5000/api/messages", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    const messages = await response.json();
    const messageList = document.getElementById("message-list");

    messages.forEach((message) => {
        const messageItem = document.createElement("div");
        messageItem.innerHTML = `
            <p><strong>${message.sender}: </strong>${message.content}</p>
        `;
        messageList.appendChild(messageItem);
    });
}

// Send Message
document.getElementById("sendMessage").addEventListener("click", async () => {
    const messageContent = document.getElementById("messageInput").value;

    const response = await fetch("http://127.0.0.1:5000/api/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: messageContent }),
    });

    if (response.ok) {
        alert("Message sent!");
        document.getElementById("messageInput").value = ""; // Clear input field
        loadMessages(); // Refresh messages
    } else {
        alert("Failed to send message. Please try again.");
    }
});

// Load Messages on Page Load
document.addEventListener("DOMContentLoaded", loadMessages);