from fastapi import FastAPI, Request
import telebot
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

app = FastAPI()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "👋 Welcome! Your bot is now online and working.")

@bot.message_handler(commands=['strategy'])
def handle_strategy(message):
    bot.reply_to(message, "📊 Strategy: Sell 600k @0.01, 600k @0.015, 400k @0.02, rest @0.03")

@bot.message_handler(commands=['price'])
def handle_price(message):
    bot.reply_to(message, "💰 Price targets: 0.015 / 0.02 / 0.03")

@bot.message_handler(commands=['claim'])
def handle_claim(message):
    bot.reply_to(message, "📦 Claim not open yet. Expected ~21:30 UTC+8")

@bot.message_handler(commands=['next'])
def handle_next(message):
    bot.reply_to(message, "🚀 Next: Cogni AI / Lightchain AI. Use /strategy for plan.")

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.body()
    update = telebot.types.Update.de_json(data.decode("utf-8"))
    bot.process_new_updates([update])
    return "ok"