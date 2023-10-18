/*!
* Start Bootstrap - Coming Soon v6.0.7 (https://startbootstrap.com/theme/coming-soon)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-coming-soon/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(document).ready(function() {
    $("#submitButton").click(function() {
        $("#text").text("Results are coming!");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("fileInput");
    const fileInput = document.getElementById("pdf-file-input");
    const uploadButton = document.getElementById("submitButton");
    const uploadStatus = document.getElementById("submitSuccessMessage");

    uploadButton.addEventListener("click", function () {
        if (fileInput.files.length === 0) {
            uploadStatus.innerText = "Please select a PDF file to upload.";
            return;
        }

        const formData = new FormData();
        formData.append("pdf_file", fileInput.files[0]);

        fetch("/upload-resume/", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                uploadStatus.innerText = "File uploaded successfully!";
                // You can handle the response from the server here
            })
            .catch((error) => {
                uploadStatus.innerText = "Error uploading the file.";
                console.error("Error:", error);
            });
    });
});
