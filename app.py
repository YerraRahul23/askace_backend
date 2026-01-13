from flask import Flask, request, jsonify
from model import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return "AskAce Backend is running 🚀"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = get_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
