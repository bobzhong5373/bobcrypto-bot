from fastapi import FastAPI, Request
import telebot
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

app = FastAPI()

# 指令响应
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! Your bot is now online and working.")

@bot.message_handler(commands=['strategy'])
def send_strategy(message):
    bot.reply_to(message, "📊 Current strategy: Sell 600k @0.01, 600k @0.015, 400k @0.02, rest @0.03")

@bot.message_handler(commands=['price'])
def send_price(message):
    bot.reply_to(message, "💰 Current price targets: 0.015 / 0.02 / 0.03 with dynamic adjustment.")

@bot.message_handler(commands=['claim'])
def send_claim(message):
    bot.reply_to(message, "📦 Claim not open yet. Estimated: Tonight ~21:30 (UTC+8)")

@bot.message_handler(commands=['next'])
def send_next(message):
    bot.reply_to(message, "🚀 Next: Cogni AI / Lightchain AI. Use /strategy for exit plan.")

# FastAPI 用于接收 webhook
@app.post("/webhook")
async def process_webhook(request: Request):
    if request.headers.get('content-type') == 'application/json':
        json_str = await request.body()
        update = telebot.types.Update.de_json(json_str.decode("utf-8"))
        bot.process_new_updates([update])
    return "ok"