// Get the scroll-to-top button
const scrollToTopButton = document.getElementById('scroll-to-top');

// When the user scrolls down 100px from the top of the document, show the button
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollToTopButton.style.display = "block"; // Show the button
    } else {
        scrollToTopButton.style.display = "none"; // Hide the button
    }
};

// When the user clicks on the button, scroll to the top
scrollToTopButton.onclick = function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth" // Smooth scrolling
    });
};


// register.js
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("register-form");
    const inputs = form.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener("blur", () => {
            if (!input.value.trim()) {
                input.classList.add("is-invalid");
            } else {
                input.classList.remove("is-invalid");
            }
        });

        input.addEventListener("focus", () => {
            input.classList.remove("is-invalid");
        });
    });
});
