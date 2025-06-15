import os
import requests
from datetime import datetime

def morning_broadcast():
    message = f"🌅 早安！今日投资播报时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    message += "- Solaxy 预售状态：监听中\n"
    message += "- 接力项目状态：Cogni、Lightchain、Ozak 正在监控\n"
    message += "- TGE 倒计时、价格提醒、链上动态同步启动 ✅"
    send_telegram(message)

def evening_broadcast():
    message = f"🌙 晚间播报时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    message += "- 今日价格播报完成 📊\n"
    message += "- 巨鲸异动监听：暂无重大转账 🐋\n"
    message += "- 明日继续提醒 ⏰"
    send_telegram(message)

def send_telegram(message):
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_USER_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"发送失败: {e}")
