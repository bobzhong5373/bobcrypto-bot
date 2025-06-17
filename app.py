from flask import Flask, request
import telebot
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # Render 设置环境变量 BOT_TOKEN
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "你好，Bot 已恢复上线 ✅")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"收到你的消息：{message.text}")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    return 'Invalid request', 403

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://你的项目名.onrender.com/webhook')  # 替换为你的真实 Render 地址
    app.run(host='0.0.0.0', port=10000)