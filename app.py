from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)
    return {"status": "ok"}

