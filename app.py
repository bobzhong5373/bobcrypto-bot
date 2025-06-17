import logging
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from flask import Flask

app = Flask(__name__)

# 日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram Token
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

bot = telegram.Bot(token=TELEGRAM_TOKEN)

# /start 指令
def start(update, context):
    update.message.reply_text("👋 欢迎使用 Bob Web3 Bot！已成功上线。")

# /simulate 模拟播报
def simulate(update, context):
    message = "**模拟播报测试**：系统运行正常 ✅"
    update.message.reply_text("📢 Telegram 播报成功 ✅")
    requests.post(DISCORD_WEBHOOK, json={"content": message})

# 错误处理
def error(update, context):
    logging.warning(f'更新 {update} 引发错误：{context.error}')

# 监听设置
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # 指令绑定
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("simulate", simulate))

    # 错误处理绑定
    dp.add_error_handler(error)

    # 启动监听（Polling 模式）
    updater.start_polling()
    updater.idle()

# Flask 保活
@app.route('/')
def keep_alive():
    return "Bot is running!"

if __name__ == '__main__':
    main()