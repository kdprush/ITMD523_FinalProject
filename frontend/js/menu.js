// Highlight Active Page in Navigation Bar
document.addEventListener("DOMContentLoaded", () => {
    const currentPage = location.pathname.split("/").pop(); // Get the current page name
    const navLinks = document.querySelectorAll("nav ul li a");

    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (href === currentPage || (currentPage === "" && href === "index.html")) {
            link.classList.add("active"); // Add 'active' class to the current page link
        } else {
            link.classList.remove("active"); // Ensure no other link has 'active'
        }
    });
});