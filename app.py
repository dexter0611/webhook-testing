from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1443700815100510288/BdBBURGQyk4ugt0ZC5VOgG84h-rW2uFzVVoveJ6nGXUPmsAsxmrKsPMakp0OaYOedj8Y"

@app.route("/")
def home():
    return "Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)

    embed = {
        "title": "📝 New Google Form Submission!",
        "description": "A new response has been submitted.",
        "color": 0x5865F2,  # Discord blurple
        "fields": [
            {"name": "Time submitted", "value": data.get("timestamp", "N/A"), "inline": False},
            {"name": "nee fill panna date", "value": data.get("res1", "N/A"), "inline": False},
            {"name": "Peru nee kuduthathu", "value": data.get("res2", "N/A"), "inline": False},
            {"name": "nalam ariya aaval", "value": data.get("res3", "N/A"), "inline": False},
            {"name": "send off message", "value": data.get("res4", "N/A"), "inline": False},
        ],
        "footer": {"text": "Automated by KV Webhook System"}
    }

    payload = {
        "username": "webhook bot ahe",
        "avatar_url": "https://cdn.discordapp.com/embed/avatars/4.png",
        "embeds": [embed]
    }

    requests.post(DISCORD_WEBHOOK, json=payload)

    return {"status": "ok"}


