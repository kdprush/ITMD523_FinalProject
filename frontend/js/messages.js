// Load Messages
async function loadMessages() {
    const response = await fetch("http://127.0.0.1:5000/api/messages", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    const messages = await response.json();
    const messageList = document.getElementById("messageList");

    messageList.innerHTML = ""; // Clear the list
    messages.forEach((message) => {
        const messageItem = document.createElement("div");
        messageItem.innerHTML = `
            <p><strong>${message.sender}:</strong> ${message.content}</p>
        `;
        messageList.appendChild(messageItem);
    });
}

// Send a Message
document.getElementById("sendMessage").addEventListener("click", async () => {
    const messageContent = document.getElementById("messageInput").value;

    const response = await fetch("http://127.0.0.1:5000/api/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: messageContent }),
    });

    if (response.ok) {
        loadMessages(); // Reload messages
        document.getElementById("messageInput").value = ""; // Clear input
    } else {
        alert("Failed to send message.");
    }
});

// Load messages when the page loads
document.addEventListener("DOMContentLoaded", loadMessages);