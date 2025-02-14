
# 🔥 AI-Powered Code Generator (Flask + Deep Learning)

This project is a **Flask-based Code Generator** that uses **Deep Learning (DL) & Machine Learning (ML)** to generate code from natural language prompts.

## 🚀 Features
- ✅ Accepts text prompts and generates code using AI models.
- ✅ Supports multiple programming languages (Python, JavaScript, etc.).
- ✅ Simple and user-friendly web interface (HTML, CSS, JavaScript).
- ✅ Backend powered by **Flask** and **Hugging Face Transformers**.
- ✅ Cross-Origin support (CORS enabled) for easy integration.

---

## 📂 Project Structure
/code-generator 
│── /static 
│      ├── style.css # Frontend styling
│      ├── script.js # Handles API calls 
│── /templates 
│      ├── index.html # Frontend UI
│── app.py # Main Flask application 
│── requirements.txt # Python dependencies 
│── README.md # Project documentation




---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/code-generator.git
cd code-generator
```
2️⃣ Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Run Flask App
```
python app.py
```
5️⃣ Open in Browser
```
Visit: http://127.0.0.1:5000/
```

# 🎯 Usage
Enter a prompt (e.g., "Write a Python function to add two numbers.").
Click "Generate Code".
The AI will generate and display the relevant code.

# 🧑‍💻 Tech Stack
Backend: Flask, Hugging Face Transformers, PyTorch
Frontend: HTML, CSS, JavaScript (Fetch API)
ML Model: Code-Generation Model (e.g., bigcode/starcoder)
# 🛠️ Troubleshooting
Common Issues & Fixes
❌ ModuleNotFoundError: No module named 'flask'
✅ Run: pip install flask

❌ CORS error in browser console
✅ Ensure flask-cors is installed and added to app.py:

from flask_cors import CORS
CORS(app)
# 🤝 Contributing
Feel free to open an issue or submit a pull request if you have improvements!

