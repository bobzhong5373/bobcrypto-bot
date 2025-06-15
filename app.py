from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# ✅ 首页测试
@app.route('/')
def home():
    return "🤖 Bot is running!"

# 🛠️ Telegram webhook 接收器
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        # 🎯 命令响应
        if text == '/start':
            send_message(chat_id, "🤖 Bot 已上线，可以开始使用了！")
        elif text == '/next':
            send_message(chat_id, "📌 当前推荐接力项目：\n1. Cogni AI\n2. Lightchain AI")
        elif text == '/claim':
            send_message(chat_id, "📥 Solaxy 当前状态：尚未开启 Claim\n🕒 请继续等待系统监控提醒")
        elif text == '/price':
            send_message(chat_id, "📈 当前 Uniswap 池子价格监控中...\n📊 初始目标挂单区间：$0.015 / $0.03")

    return {'ok': True}

# 📬 核心发信方法
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

# 🧩 启动服务并设置 webhook
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    # 设置 webhook
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    response = requests.get(telegram_url, params={"url": WEBHOOK_URL})
    print("Webhook set:", response.json())

    app.run(host='0.0.0.0', port=port)
