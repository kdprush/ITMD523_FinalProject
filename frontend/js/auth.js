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

    const data = await response.json();
    if (response.ok) {
        alert("Login successful!");
        window.location.href = data.role === "client" ? "dashboard-client.html" : "dashboard-freelancer.html";
    } else {
        alert(data.message);
    }
});

// Signup Form Submission
document.getElementById("signupForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("emailSignup").value;
    const password = document.getElementById("passwordSignup").value;
    const role = document.querySelector('input[name="role"]:checked').value;

    const response = await fetch("http://127.0.0.1:5000/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password, role }),
    });

    if (response.ok) {
        alert("Sign-up successful! Please log in.");
    } else {
        const error = await response.json();
        alert(error.message);
    }
});