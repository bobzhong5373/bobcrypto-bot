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

# webhook 接收器
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').lower()

        if text == '/start':
            send_message(chat_id, "🤖 Bot 已上线，可以开始使用了！")

        elif text == '/next':
            send_message(chat_id, "📌 当前推荐项目：\n1. Cogni AI\n2. Lightchain AI\n3. Ozak AI（备选）")

        elif text == '/claim':
            send_message(chat_id, "📥 Solaxy Claim 状态：\n尚未开放，预期为 6月16日 21:30 后启动。\n请耐心等待 Bot 推送提醒。")

        elif text == '/price':
            send_message(chat_id, "📊 当前建议挂单：\n- $0.015：保本提醒\n- $0.03：高位目标\n（Claim 后将自动追踪 Uniswap 价格）")

        elif text == '/strategy':
            send_message(chat_id, "📈 当前挂单策略模板：\n持仓：1,911,324 SOLX\n目标：$30,000\n分批挂单如下：\n- $0.015 卖出 20%\n- $0.02 卖出 30%\n- $0.03 卖出 50%")

    return {'ok': True}

# 发消息方法
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

# 启动服务 & 设置 webhook
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    response = requests.get(telegram_url, params={"url": WEBHOOK_URL})
    print("Webhook 设置结果：", response.json())
    app.run(host='0.0.0.0', port=port)
