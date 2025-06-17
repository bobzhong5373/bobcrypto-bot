import os
import telegram
from telegram.ext import Updater, CommandHandler
import requests

# Telegram token from environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# 初始化 Telegram bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# 指令回应函数
def start(update, context):
    update.message.reply_text("🤖 你好，我是 Web3 投资提醒机器人！输入 /next 查看最新推荐项目。")

def claim(update, context):
    update.message.reply_text("📦 Solaxy Claim 功能正在监听中，启动后我会提醒你！")

def price(update, context):
    update.message.reply_text("💰 当前挂单监控中，默认价格提醒为 $0.015 / $0.02 / $0.03")

def strategy(update, context):
    update.message.reply_text("📊 当前策略为：目标$30,000，分批挂单建议已设定。")

def next_project(update, context):
    update.message.reply_text("🚀 当前推荐接力项目：\n1. Cogni AI\n2. Lightchain AI\n3. Ozak AI")

# Discord Webhook 通知测试函数
def send_to_discord(message):
    if DISCORD_WEBHOOK:
        try:
            requests.post(DISCORD_WEBHOOK, json={"content": message})
        except Exception as e:
            print(f"❌ Discord 推送失败: {e}")

# 主函数
def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # 添加指令处理器
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("claim", claim))
    dp.add_handler(CommandHandler("price", price))
    dp.add_handler(CommandHandler("strategy", strategy))
    dp.add_handler(CommandHandler("next", next_project))

    # 启动 polling
    updater.start_polling()
    send_to_discord("✅ Bot 启动成功，开始监听 Telegram 指令。")
    updater.idle()

if __name__ == '__main__':
    main()