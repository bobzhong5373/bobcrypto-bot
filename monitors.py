import requests
import os

# 示例价格监听
def check_price():
    try:
        # 示例地址（你可以改为任意 DEX 接口）
        response = requests.get("https://api.dexscreener.com/latest/dex/pairs/ethereum/0x0000000000000000000000000000000000000000")
        data = response.json()
        price = float(data["pair"]["priceUsd"])
        print(f"[价格监听] 当前价格: {price}")
        # 示例阈值提醒
        if price >= 0.03:
            send_telegram_alert(f"🚨 价格突破 0.03，当前价格：{price}")
    except Exception as e:
        print(f"价格监听异常: {e}")

# 示例鲸鱼动态监听（模拟）
def check_whale_activity():
    try:
        # 可换成链上追踪接口，如 Etherscan、Arkham 等
        print("[鲸鱼监听] 正在模拟检查...")
        # 示例提醒
        send_telegram_alert("🐋 检测到鲸鱼地址资金异动！")
    except Exception as e:
        print(f"鲸鱼监听异常: {e}")

def send_telegram_alert(message):
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
        print(f"Telegram 推送失败: {e}")
