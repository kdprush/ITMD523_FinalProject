// auth.js: Handles Login and Signup

// Login Form Submission
document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
        const data = await response.json();
        alert("Login successful!");
        window.location.href = data.role === "client" ? "dashboard-client.html" : "dashboard-freelancer.html";
    } else {
        alert("Login failed. Please check your credentials.");
    }
});

// Signup Form Submission
document.getElementById("signupForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("emailSignup").value;
    const password = document.getElementById("passwordSignup").value;

    const response = await fetch("http://127.0.0.1:5000/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
    });

    if (response.ok) {
        alert("Signup successful! Please log in.");
    } else {
        alert("Signup failed. Please try again.");
    }
});