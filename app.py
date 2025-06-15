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

        # 🎯 命令响应逻辑
        if text == '/start':
            send_message(chat_id, "🤖 Bot 已就绪，请输入命令：\n/start\n/next\n/price\n/strategy")
        elif text == '/next':
            send_message(chat_id, "📌 当前推荐项目：\n1. Cogni AI\n2. Lightchain AI")
        elif text == '/claim':
            send_message(chat_id, "📢 Solaxy 仍未开启 Claim，请稍后再试。")
        elif text == '/price':
            send_message(chat_id, "💰 当前挂单价格为：\n0.015 / 0.02 / 0.03\n请根据实际行情调整。")
        elif text == '/strategy':
            send_message(chat_id, "📈 当前分批卖出策略：\n30% - 0.015\n40% - 0.02\n30% - 0.03")
    
    return {'ok': True}

# 📬 核心发信函数
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    print(response.text)

# 🔗 启动监听服务 + Webhook 注册
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    # 设置 Webhook（仅部署时自动运行）
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    requests.get(telegram_url, params={"url": WEBHOOK_URL})
    print("✅ Webhook 已设置成功")

    # 可选测试推送（上线后自动推送）
    send_message(USER_ID, "✅ 测试提醒已发送 – Bot 成功部署！")

    app.run(host='0.0.0.0', port=port)
