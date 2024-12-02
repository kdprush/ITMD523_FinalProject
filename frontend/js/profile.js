// Load User Profile
async function loadProfile() {
    const response = await fetch("http://127.0.0.1:5000/api/users/profile", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    const user = await response.json();
    document.getElementById("name").value = user.name;
    document.getElementById("email").value = user.email;
}

// Update User Profile
document.getElementById("updateProfileForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const newPassword = document.getElementById("newPassword").value;

    const response = await fetch("http://127.0.0.1:5000/api/users/profile", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, password: newPassword }),
    });

    if (response.ok) {
        alert("Profile updated successfully!");
    } else {
        alert("Failed to update profile.");
    }
});

// Load profile when the page loads
document.addEventListener("DOMContentLoaded", loadProfile);