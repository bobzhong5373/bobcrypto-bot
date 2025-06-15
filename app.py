from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# ✅ 首页测试接口
@app.route('/')
def home():
    return "🤖 Bot is running!"

# 🛠️ Telegram Webhook 接收器
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        # 🎯 指令响应逻辑
        if text == '/start':
            send_message(chat_id, "🤖 Bot 已上线！输入 /next 查看接力项目")
        elif text == '/next':
            send_message(chat_id, "📌 当前推荐项目：\n\n🚀 Cogni AI\n💡 Lightchain AI\n🧠 Ozak AI")
        elif text == '/claim':
            send_message(chat_id, "📢 Solaxy Claim 状态：尚未开放，预计 6 月 16 日晚间启动")
        elif text == '/price':
            send_message(chat_id, "💰 当前挂单建议：\n• $0.015（保本）\n• $0.03（冲高止盈）")
        elif text == '/strategy':
            send_message(chat_id, "📈 分批卖出策略：\n• 40% 挂 0.015\n• 40% 挂 0.03\n• 20% 留作后续观察")
    
    return {'ok': True}

# 📤 核心发信函数
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    print(response.text)

# 🚀 启动监听服务 + 设置 Webhook
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    # 设置 Webhook（仅部署时自动运行一次）
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    requests.get(telegram_url, params={"url": f"{WEBHOOK_URL}"})
    print("✅ Webhook 已设置成功")

    # 测试推送（上线时自动发一次）
    send_message(USER_ID, "✅ 测试提醒已发送 – Bot 成功部署！")

    app.run(host='0.0.0.0', port=port)
