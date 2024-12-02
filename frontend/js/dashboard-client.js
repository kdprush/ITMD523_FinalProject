// Load Client's Jobs
async function loadJobs() {
    const response = await fetch("http://127.0.0.1:5000/api/jobs", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    const jobs = await response.json();
    const jobList = document.getElementById("jobList");

    jobList.innerHTML = ""; // Clear the list
    jobs.forEach((job) => {
        const jobItem = document.createElement("div");
        jobItem.innerHTML = `
            <h3>${job.title}</h3>
            <p>${job.description}</p>
            <p>Budget: $${job.budget}</p>
        `;
        jobList.appendChild(jobItem);
    });
}

// Post a New Job
document.getElementById("jobPostForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = document.getElementById("jobTitle").value;
    const description = document.getElementById("jobDescription").value;
    const budget = document.getElementById("jobBudget").value;

    const response = await fetch("http://127.0.0.1:5000/api/jobs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description, budget }),
    });

    if (response.ok) {
        alert("Job posted successfully!");
        loadJobs(); // Reload jobs
    } else {
        alert("Failed to post job. Please try again.");
    }
});

// Load jobs when the page loads
document.addEventListener("DOMContentLoaded", loadJobs);