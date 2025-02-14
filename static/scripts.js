function generateCode() {
    let prompt = document.getElementById("prompt").value;
    let output = document.getElementById("output");

    output.textContent = "Generating code...";

    fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
        if (data.generated_code) {
            output.textContent = data.generated_code;
        } else {
            output.textContent = "Error: " + data.error;
        }
    })
    .catch(error => {
        output.textContent = "Request failed.";
    });
}
