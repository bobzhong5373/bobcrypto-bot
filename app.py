from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")  # 你的 Telegram 数字 ID
WEBHOOK_URL = "https://你的项目名.up.railway.app/webhook"  # ⚠️ 替换为你的实际 Railway 地址

# 首页用于测试部署
@app.route('/')
def home():
    return "🤖 Bot is running!"

# Telegram webhook 接收器
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        # 处理 /start 指令
        if text.lower() == '/start':
            send_message(chat_id, "🤖 Bot 已上线，可以开始使用了！")
    return {'ok': True}

# 核心发送方法
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == '__main__':
    # 自动设置 webhook
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    r = requests.get(telegram_url, params={"url": WEBHOOK_URL})
    print("Webhook 设置结果:", r.json())

    # 启动时发送测试提醒
    if BOT_TOKEN and USER_ID:
        send_message(USER_ID, "✅ 测试提醒：你的 Bot 已部署并成功启动")

    # 启动服务
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
