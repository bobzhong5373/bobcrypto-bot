import os
from flask import Flask, request
import telegram
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# ✅ 从环境变量获取 Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route('/')
def home():
    return "BOBcrypto Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    message = update.message or update.edited_message

    if message:
        text = message.text or ""
        chat_id = message.chat.id

        if text.startswith('/start'):
            bot.send_message(chat_id=chat_id, text="✅ BOBcrypto Bot 已启动，你将收到 Web3 投资提醒。")

    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
