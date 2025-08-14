from flask import Flask, request
import requests

app = Flask(__name__)

# Tokenul tău Blynk
BLYNK_TOKEN = "hueAZAw4qXtTBS9FQ8ZsYjGDwJHWwMe8"  # înlocuiește cu tokenul tău real

@app.route('/proxy', methods=['GET'])
def proxy():
    # Preia parametrii din URL
    virtual_pin = request.args.get('v', '1')  # v1, v2, etc.
    value = request.args.get('value', '1')    # 1 sau 0

    # URL-ul real Blynk
    blynk_url = f"https://fra1.blynk.cloud/external/api/update?token={BLYNK_TOKEN}&{virtual_pin}={value}"

    try:
        resp = requests.get(blynk_url)
        return resp.text, resp.status_code
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
