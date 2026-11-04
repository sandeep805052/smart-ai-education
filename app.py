from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "response": "Please enter a question."
        }), 400

    bot_response = get_response(user_message)

    return jsonify({
        "response": bot_response
    })


if __name__ == "__main__":
    app.run(debug=True)