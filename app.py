import os
import telegram
from telegram.ext import Updater, CommandHandler
from flask import Flask, request
import requests

# 读取环境变量
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

app = Flask(__name__)

# Telegram Bot 初始化
bot = telegram.Bot(token=TELEGRAM_TOKEN)

def start(update, context):
    update.message.reply_text('🤖 你的 bot 已上线，欢迎使用！')

def simulate(update, context):
    update.message.reply_text('📢 模拟播报：Solaxy 项目已启动 Claim。请准备挂单。')
    # 同步发送到 Discord
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": "📢 模拟播报：Solaxy 项目已启动 Claim。请准备挂单。"})

def unknown(update, context):
    update.message.reply_text("❓ 指令未识别，请使用 /start 或 /simulate。")

# 设置指令监听
@app.route('/')
def index():
    return "Bot 正在运行中..."

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("simulate", simulate))
    dispatcher.add_handler(CommandHandler(None, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()