// dashboard.js: Handles Client and Freelancer Dashboards

// Load Jobs for Clients or Freelancers
async function loadJobs() {
    const response = await fetch("http://127.0.0.1:5000/api/jobs", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    const jobs = await response.json();
    const jobList = document.getElementById("job-list");

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

// Post Job for Clients
if (document.getElementById("jobPostForm")) {
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
            loadJobs(); // Refresh job list
        } else {
            alert("Failed to post job. Please try again.");
        }
    });
}

// Load Jobs on Page Load
document.addEventListener("DOMContentLoaded", loadJobs);