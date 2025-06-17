import os
import telegram
from telegram.ext import Updater, CommandHandler
import requests
from flask import Flask

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🤖 Hello! I'm your Web3 bot.")

def simulate(update, context):
    message = "**[🧪 模拟提醒]**\nSolaxy 已启动 Claim，请尽快挂单！\n挂单建议价格：0.015 / 0.02 / 0.03"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='Markdown')
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": message})

@app.route('/')
def home():
    return "Bot is running."

def run_telegram_bot():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("simulate", simulate))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run_telegram_bot()