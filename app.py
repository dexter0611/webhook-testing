from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1443698733144608869/E636QSbLv8k_PuYOt8WW7YuvWMLhCjHfgeoNvOAYSoRwtOWVSZZyegmNqHpwJ67JhzJZ"

@app.route("/")
def home():
    return "Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)

    # Create message for Discord
    message = (
        "**New Google Form Submission!**\n"
        f"**Date:** {data.get('timestamp')}\n"
        f"**Response 1:** {data.get('res1')}\n"
        f"**Response 2:** {data.get('res2')}\n"
        f"**Response 3:** {data.get('res3')}\n"
        f"**Response 4:** {data.get('res4')}"
    )

    # Send message to Discord
    requests.post(DISCORD_WEBHOOK, json={"content": message})

    return {"status": "ok"}
