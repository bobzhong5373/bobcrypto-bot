
from fastapi import FastAPI, Request
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = FastAPI()

# 定义命令处理函数
def start(update, context):
    update.message.reply_text("👋 Welcome! Your bot is now online and working.")

def strategy(update, context):
    update.message.reply_text("📊 Current strategy: Sell 600k @0.01, 600k @0.015, 400k @0.02, rest @0.03")

def price(update, context):
    update.message.reply_text("💰 Current price targets: 0.015 / 0.02 / 0.03 with dynamic adjustment based on Uniswap data.")

def claim(update, context):
    update.message.reply_text("📦 Claim not open yet. Estimated time: Tonight around 21:30 (UTC+8). Stay tuned!")

def next(update, context):
    update.message.reply_text("🚀 Next project recommendation: Cogni AI or Lightchain AI. Use /strategy for exit plan.")

dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("strategy", strategy))
dispatcher.add_handler(CommandHandler("price", price))
dispatcher.add_handler(CommandHandler("claim", claim))
dispatcher.add_handler(CommandHandler("next", next))

@app.post("/webhook")
async def webhook(request: Request):
    json_data = await request.json()
    update = telegram.Update.de_json(json_data, bot)
    dispatcher.process_update(update)
    return "ok"

@app.get("/")
def root():
    return {"status": "Bot is live."}
