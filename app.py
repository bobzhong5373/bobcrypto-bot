import os
import telegram
from telegram.ext import Updater, CommandHandler
import requests

# 获取环境变量
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# 初始化 Telegram Bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# 定义命令处理函数
def start(update, context):
    message = "🤖 你好！我是你的 Web3 投资提醒机器人。\n\n可用指令：\n/start\n/next\n/strategy\n/price\n/claim"
    update.message.reply_text(message)
    notify_discord(f"📥 用户启动了 /start 指令：{update.effective_user.username}")

def next_project(update, context):
    message = "📊 当前推荐项目：\n1. Cogni AI（预计 TGE：6月内）\n2. Lightchain AI（技术优势明显）\n3. Ozak AI（结构合理）"
    update.message.reply_text(message)
    notify_discord(f"📡 推送 /next 项目推荐")

def strategy(update, context):
    message = "📌 当前挂单策略：\n- $0.015: 30%仓位\n- $0.02: 40%仓位\n- $0.03: 30%仓位\n\n如需调整，请使用后台界面。"
    update.message.reply_text(message)
    notify_discord(f"📐 用户查看 /strategy 策略")

def price(update, context):
    message = "💰 当前挂单价格监听：\n✅ $0.015（提醒）\n✅ $0.02（提醒）\n✅ $0.03（提醒）"
    update.message.reply_text(message)
    notify_discord("🔔 用户查询 /price 挂单价格")

def claim(update, context):
    message = "🧾 Solaxy Claim 状态：尚未开启（预计 6月17日）\n我将实时监听 Claim 启动信号并提醒你。"
    update.message.reply_text(message)
    notify_discord("📣 用户触发 /claim 查询")

# 推送消息到 Discord
def notify_discord(content):
    if DISCORD_WEBHOOK:
        try:
            requests.post(DISCORD_WEBHOOK, json={"content": content})
        except:
            print("❌ Discord 推送失败")

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # 绑定命令
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("next", next_project))
    dispatcher.add_handler(CommandHandler("strategy", strategy))
    dispatcher.add_handler(CommandHandler("price", price))
    dispatcher.add_handler(CommandHandler("claim", claim))

    # 启动轮询
    updater.start_polling()
    print("🤖 Bot 正在运行中（使用 polling 保活）")
    updater.idle()

if __name__ == "__main__":
    main()