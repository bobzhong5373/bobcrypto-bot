from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text.lower() == '/start':
            send_message(chat_id, "🤖 Bot 已上线，可以开始使用了！")

    return {'ok': True}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    # ✅ 最关键的修改：固定 webhook 地址
    webhook_url = "https://web-production-7f5d.up.railway.app/webhook"
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"

    response = requests.get(telegram_url, params={"url": webhook_url})
    print("Webhook set:", response.json())

    app.run(host='0.0.0.0', port=port)
