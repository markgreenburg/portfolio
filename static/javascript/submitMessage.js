'use strict';
window.onload = () => {
    const contactForm = $("#contact-form");
    const button = $("button#submit-btn");
    // Handle contact form submissions and client response
    contactForm.on("submit", (event) => {
        event.preventDefault();
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
                contactForm.trigger("reset");
                button.html("Sent! <i class='fa fa-check-circle'></i>");
                $("div#form-err-msg").remove();
            },
            error: (err) => {
                $("form#contact-form").append(`
                <div id='form-err-msg'><p>Sorry, the robots messed up! Please 
                submit again or email me directly at 
                <a href="mailto:mark@markgreenburg.com">
                mark@markgreenburg.com</a>.</p></div>`);
                button.html("Send <i class='fa fa-arrow-right'></i>");
            },
        });
    });

    // Reset button if form contents changed
    contactForm.children().on("keypress", () => {
        button.html("Send <i class='fa fa-arrow-right'></i>");
    });
};