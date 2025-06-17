import os
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

from flask import Flask

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 你好，我是 Bob 的提醒机器人，已成功上线！")

def next_command(update: Update, context: CallbackContext):
    message = "📊 当前推荐接力项目：\n\n🚀 **Cogni AI**\n🔹 TGE 倒计时：3天内\n🔹 上线平台：MEXC\n🔹 风险评级：中低\n\n如需完整策略，请输入 /strategy"
    update.message.reply_text(message)
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": message})

def strategy_command(update: Update, context: CallbackContext):
    message = "📈 当前挂单策略：\n\n1️⃣ $0.015 - 出售 30%\n2️⃣ $0.02 - 出售 40%\n3️⃣ $0.03 - 出售 30%\n\n📍动态调整策略请关注 Bot 实时提醒。"
    update.message.reply_text(message)

@app.route("/")
def home():
    return "Bot is running!"

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("next", next_command))
    dispatcher.add_handler(CommandHandler("strategy", strategy_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main() 