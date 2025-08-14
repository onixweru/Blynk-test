from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Tokenul Blynk (înlocuiește cu al tău)
BLYNK_TOKEN = "hueAZAw4qXtTBS9FQ8ZsYjGDwJHWwMe8"
BLYNK_BASE_URL = "https://fra1.blynk.cloud/external/api/update"

@app.route("/start", methods=["GET"])
def start_device():
    try:
        url = f"{BLYNK_BASE_URL}?token={BLYNK_TOKEN}&v1=1"
        r = requests.get(url)
        return jsonify({"status": "started", "blynk_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/stop", methods=["GET"])
def stop_device():
    try:
        url = f"{BLYNK_BASE_URL}?token={BLYNK_TOKEN}&v1=0"
        r = requests.get(url)
        return jsonify({"status": "stopped", "blynk_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "API-ul Blynk este online!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
