
import os
import requests
# import imghdr
# from telegram.files.inputfile import InputFile  # 当前版本未使用

# 启用日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 获取环境变量
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

# 定义启动命令
def start(update, context):
    update.message.reply_text("👋 Hello! 你的 Bot 已上线，可接收提醒。")
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
