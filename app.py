import logging
from telegram.ext import Updater, CommandHandler
import os
import requests
# from telegram.files.inputfile import InputFile  # 暂时注释掉

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def start(update, context):
    update.message.reply_text("👋 Hello! 你的 Bot 已上线，可接收提醒。")
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": "✅ Telegram Bot 已成功启动并响应 /start 指令。"})

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
