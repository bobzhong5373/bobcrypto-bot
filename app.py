from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # 如部署在 Railway，需手动设置

# 🟢 首页测试
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

        # 🧾 命令匹配响应
        if text == '/start':
            send_message(chat_id, "🤖 Bot 已上线，可以开始使用了！")

        elif text == '/next':
            send_message(chat_id, "📌 当前推荐接力项目：\n1. Cogni AI\n2. Lightchain AI\n3. Ozak AI\n\n你可以输入 /claim 查看 Solaxy 状态，或输入 /strategy 查看当前挂单方案。")

        elif text == '/claim':
            send_message(chat_id, "📬 Solaxy Claim 状态：\n当前状态：等待 TGE\n预计时间：6月16日 21:30（UTC+8）\n我会在启动前自动提醒你。")

        elif text == '/price':
            send_message(chat_id, "📈 当前价格监听说明：\n我已启动 Uniswap 价格追踪系统。\n挂单提醒阈值为 $0.015 与 $0.03，成交后会自动提醒你。")

        elif text == '/strategy':
            send_message(chat_id, "🧠 当前挂单策略：\n1️⃣ $0.015（锁回成本）\n2️⃣ $0.025（中段止盈）\n3️⃣ $0.030（实现 $30,000 目标）\n\n可根据行情随时调整。")

    return {'ok': True}

# ✅ 核心发信方法
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

# ✅ 启动 Webhook + 本地监听（适配 Railway）
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    webhook_url = WEBHOOK_URL
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    response = requests.get(telegram_url, params={"url": webhook_url})
    print("Webhook set:", response.json())

    app.run(host='0.0.0.0', port=port)
