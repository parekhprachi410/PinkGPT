from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [{"role":"system", "content":"You are a helpful AI assistant."}]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    messages.append({"role":"user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    ai_reply = response.choices[0].message.content
    messages.append({"role":"assistant", "content": ai_reply})

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000
    )
