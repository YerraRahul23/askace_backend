from flask import Flask, request, jsonify
from model import get_answer
from gemini import format_answer

app = Flask(__name__)

USE_GEMINI_KEYWORDS = {
    "fee", "fees", "placement", "package", "salary",
    "club", "sports", "fest"
}

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    question = data.get("question", "").lower().strip()

    result = get_answer(question)

    if not result:
        return jsonify({
            "answer": "Sorry, I couldn’t understand your question."
        }), 200

    intent, raw_text = result

    USE_GEMINI_KEYWORDS = {
        "fee", "fees", "placement", "package", "salary",
        "club", "sports", "fest"
    }

    try:
        if any(word in question for word in USE_GEMINI_KEYWORDS):
            final_answer = format_answer(question, raw_text)
        else:
            final_answer = raw_text
    except Exception as e:
        print("Gemini fallback used:", e)
        final_answer = raw_text  # ⬅️ GUARANTEED fallback

    # ✅ ALWAYS RETURN A RESPONSE
    return jsonify({
        "answer": final_answer
    }), 200



@app.route("/", methods=["GET"])
def home():
    return "AskAce Backend is Running 🚀"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
