from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin access

# Load the Code Generation Model
code_generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_code():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Generate code from the prompt
        result = code_generator(prompt, max_length=150, num_return_sequences=1)
        generated_code = result[0]["generated_text"]

        return jsonify({"generated_code": generated_code})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)