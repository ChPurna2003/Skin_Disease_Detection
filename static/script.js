const form = document.getElementById("uploadForm");
const diagnosisBox = document.getElementById("diagnosis");
const fileInput = document.getElementById("fileInput");

fileInput.addEventListener("change", () => {
    diagnosisBox.innerText = "Image selected. Click Analyze.";
});

form.addEventListener("submit", async function(e) {
    e.preventDefault();

    if (!fileInput.files[0]) {
        diagnosisBox.innerText = "Please upload an image!";
        return;
    }

    diagnosisBox.innerText = "Analyzing... Please wait.";

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    let res = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    if (data.predictions && data.predictions.length > 0) {
        diagnosisBox.innerText =
            data.predictions[0].class.toUpperCase() +
            " (" + (data.predictions[0].confidence * 100).toFixed(2) + "%)";
    } else {
        diagnosisBox.innerText = "No disease detected.";
    }
});
