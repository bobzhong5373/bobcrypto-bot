from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# 首页测试
@app.route('/')
def home():
    return "🤖 Bot is running!"

# Webhook 入口
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            send_message(chat_id, "🤖 Bot 已上线！欢迎使用投资提醒系统。")
        elif text == '/next':
            send_message(chat_id, "📌 当前推荐项目：Solaxy / Cogni AI 等，输入 /strategy 查看策略。")
        elif text == '/claim':
            send_message(chat_id, "📢 Solaxy Claim 功能已启动！请尽快挂单！")
        elif text == '/price':
            send_message(chat_id, "💰 当前挂单价位：0.015 / 0.02 / 0.03，支持分批止盈")
        elif text == '/strategy':
            send_message(chat_id, "📈 当前分批策略：30% - 0.015、50% - 0.02、20% - 0.03")
    
    return {'ok': True}

# 发送消息函数
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    print(response.text)

# 自动注册 Webhook
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    requests.get(telegram_url, params={"url": WEBHOOK_URL})
    print("✅ Webhook 已设置成功")

    send_message(USER_ID, "✅ 测试提醒已发送 – Bot 成功部署！")

    app.run(host='0.0.0.0', port=port)
