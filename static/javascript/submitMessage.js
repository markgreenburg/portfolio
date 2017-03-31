'use strict';
window.onload = () => {
    const contactForm = $("#contact-form")
    contactForm.on("submit", (event) => {
        event.preventDefault();
        const button = $("button#submit-btn");
        button.html("(This might take a sec) <i class='fa fa-spinner fa-spin'></i>");
        const formData = {
            "name": $("input#name").val(),
            "email": $("input#email").val(),
            "message": $("textarea#message").val()
        };
        $.ajax({
            type: "POST",
            url: "/submit",
            data: formData,
            encode: true,
            success: (response) => {
                // 1. Clear the form
                contactForm.trigger("reset");
                // 2. Show a confirmation
                button.html("Sent! <i class='fa fa-check-circle'></i>");
                // 3. Hide the form again(?)
            },
            error: (err) => {
                // 1. Show an error message
                // 2. Log the error
            }
        });
    });
};

/* Toggles visibility of the contact form */
const toggleForm = () => {
    const contactForm = document.getElementById("contact-form-div");
    const { display } = contactForm.style;
    if (display === 'none' || !display) {
        contactForm.style.display = 'inline-block';
    } else {
        contactForm.style.display = 'none';
    }
};