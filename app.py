import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

app = Flask(__name__)

# 从环境变量获取 Token
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

# 设置 Dispatcher
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

# /start 指令处理函数
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="🤖 Hello! 你的 Bot 已部署成功！")

# 注册指令处理器
dispatcher.add_handler(CommandHandler("start", start))

# Webhook 路由处理
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "OK"

# 主入口（仅用于测试或本地）
if __name__ == "__main__":
    app.run(debug=True)
