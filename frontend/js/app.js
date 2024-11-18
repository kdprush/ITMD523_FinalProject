// JavaScript for handling form submissions

// Handle Login Form Submission
document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    if (response.ok) {
        alert("Login successful!");
        // Redirect to dashboard
        window.location.href = "dashboard-client.html"; // Adjust based on role
    } else {
        alert(`Login failed: ${data.message}`);
    }
});

// Handle Signup Form Submission
document.getElementById("signupForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("emailSignup").value;
    const password = document.getElementById("passwordSignup").value;

    const response = await fetch("http://localhost:5000/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password })
    });

    const data = await response.json();
    if (response.ok) {
        alert("Signup successful! Please log in.");
    } else {
        alert(`Signup failed: ${data.message}`);
    }
});