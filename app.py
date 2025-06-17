import logging
from telegram.ext import Updater, CommandHandler
import os
import requests

# 启用日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 获取环境变量
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

# 定义启动指令
def start(update, context):
    update.message.reply_text("👋 Hello! 你的 Bot 已上线，可接收提醒。")
    # 同步发送到 Discord
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": "✅ Telegram Bot 已成功启动并响应 /start 指令。"})

# 主函数入口
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
