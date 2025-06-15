import os
from flask import Flask, request
import telegram
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler

app = Flask(__name__)

# 从环境变量中读取 Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route("/")
def home():
    return "Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    message = update.message or update.edited_message

    if message and message.text:
        text = message.text.strip()
        chat_id = message.chat.id

        # 简单响应指令
        if text == "/start":
            bot.send_message(chat_id=chat_id, text="✅ 欢迎使用 BOBcrypto 投资提醒 Bot！")

    return "OK"

if __name__ == "__main__":
    app.run(port=5000)
