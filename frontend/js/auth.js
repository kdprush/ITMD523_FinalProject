// Handles Sign-Up
document.getElementById("signupForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("emailSignup").value;
    const password = document.getElementById("passwordSignup").value;
    const role = document.getElementById("role").value;

    const response = await fetch("http://127.0.0.1:5000/api/users/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password, role }),
    });

    if (response.ok) {
        alert("Sign-up successful! Please log in.");
        window.location.href = "index.html";
    } else {
        const error = await response.json();
        alert(error.message || "Sign-up failed.");
    }
});

// Handles Login
document.getElementById("loginForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/api/users/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (response.ok) {
        alert("Login successful!");
        if (data.role === "client") {
            window.location.href = "dashboard-client.html";
        } else {
            window.location.href = "dashboard-freelancer.html";
        }
    } else {
        alert(data.message || "Login failed.");
    }
});