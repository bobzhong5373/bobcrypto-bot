import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 欢迎使用 BOBcrypto 投资提醒 Bot！请输入指令开始使用。")

@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "📊 当前状态：监听中，无异常。")

@bot.message_handler(commands=['next'])
def send_next(message):
    bot.reply_to(message, "🪙 今日推荐项目：\n1. Cogni AI\n2. Lightchain AI\n3. Ozak AI\nTGE 临近，关注池子动态。")

@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv("RAILWAY_WEBHOOK_URL"))
    return "Webhook set", 200

if __name__ == "__main__":
    app.run()
