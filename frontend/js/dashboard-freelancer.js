// Load Available Jobs
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
            <button onclick="applyForJob(${job.id})">Apply</button>
        `;
        jobList.appendChild(jobItem);
    });
}

// Apply for a Job
async function applyForJob(jobId) {
    const response = await fetch(`http://127.0.0.1:5000/api/jobs/${jobId}/apply`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    });

    if (response.ok) {
        alert("Applied for job successfully!");
    } else {
        alert("Failed to apply for job.");
    }
}

// Load jobs when the page loads
document.addEventListener("DOMContentLoaded", loadJobs);