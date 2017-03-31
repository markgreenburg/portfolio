'use strict';
window.onload = () => {
    $("#contact-form").on("submit", (event) => {
        event.preventDefault();
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
            success: (response) => { console.log(response) },
            error: (err) => { console.log(err) }
        });
    });
};