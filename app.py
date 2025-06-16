from fastapi import FastAPI, Request
import telebot
import os
import threading
import time

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

app = FastAPI()

@bot.message_handler(commands=['start'])
def handle_start(message):
    print("🔔 /start received from", message.chat.id)
    bot.reply_to(message, "👋 Welcome! Your bot is now online and working.")

@bot.message_handler(commands=['strategy'])
def handle_strategy(message):
    print("📊 /strategy received from", message.chat.id)
    bot.reply_to(message, "📊 Strategy: Sell 600k @0.01, 600k @0.015, 400k @0.02, rest @0.03")

@bot.message_handler(commands=['price'])
def handle_price(message):
    print("💰 /price received from", message.chat.id)
    bot.reply_to(message, "💰 Price targets: 0.015 / 0.02 / 0.03")

@bot.message_handler(commands=['claim'])
def handle_claim(message):
    print("📦 /claim received from", message.chat.id)
    bot.reply_to(message, "📦 Claim not open yet. Expected ~21:30 UTC+8")

@bot.message_handler(commands=['next'])
def handle_next(message):
    print("🚀 /next received from", message.chat.id)
    bot.reply_to(message, "🚀 Next: Cogni AI / Lightchain AI. Use /strategy for plan.")

@app.post("/webhook")
async def webhook(request: Request):
    print("✅ Webhook triggered")
    data = await request.body()
    update = telebot.types.Update.de_json(data.decode("utf-8"))
    bot.process_new_updates([update])
    print("✅ Update processed")
    return "ok"

# 保活线程，防止 Railway 自动停止服务
def keep_alive():
    while True:
        time.sleep(30)

threading.Thread(target=keep_alive).start()