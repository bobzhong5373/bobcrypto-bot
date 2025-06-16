import os
from telegram.ext import Updater, CommandHandler
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# /start 命令处理函数
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
        text="✅ 欢迎使用 BOBcryptoNotifier_bot\n\n你可以输入 /status 查看监听状态，或 /next 获取最新推荐项目。")

# 注册处理器
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Flask 应用用于接收 Telegram Webhook
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json(force=True)
    if update:
        updater.bot.process_new_updates([updater.bot.de_json(update, updater.bot)])
    return 'ok'

# 启动本地监听（仅供调试，不影响 Railway 部署）
if __name__ == '__main__':
    app.run(port=8080)
