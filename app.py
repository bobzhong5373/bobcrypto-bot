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
            send_message(chat_id, "🤖 Bot 已上线，可以开始使用！")

        elif text == '/next':
            send_message(chat_id, "📌 当前推荐接力项目：\n1. Cogni AI\n2. Lightchain AI\n3. Ozak AI\n（TGE预计7日内，可使用 /strategy 查看挂单建议）")

        elif text == '/claim':
            send_message(chat_id, "📬 Solaxy 当前状态：\n- ✅ 预售进行中，预计 6月16日 21:30 Claim\n- 可关注价格提醒模块 /price")

        elif text == '/price':
            send_message(chat_id, "💰 当前挂单策略参考：\n- 初始挂单：0.015 USDT\n- 分批调高：0.02 / 0.03\n可配合自动成交提醒使用。")

        elif text == '/strategy':
            send_message(chat_id, "📈 当前分批变现策略：\n- 成本：$0.00175\n- 总持仓：1,911,324 SOLX\n- 第一目标：0.015（锁本）\n- 第二目标：0.02\n- 第三目标：0.03（冲击 $30,000）")

    return {'ok': True}

# 📬 核心发信函数
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

# 🔗 启动监听服务 + Webhook 注册
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    
    # 设置 Telegram Webhook（仅部署时执行）
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    requests.get(telegram_url, params={"url": WEBHOOK_URL})
    print("✅ Webhook 已设置成功")

    app.run(host='0.0.0.0', port=port)
