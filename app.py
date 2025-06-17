import os
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 环境变量读取
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

# 设置日志
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start 指令响应函数
def start(update: Update, context: CallbackContext) -> None:
    welcome_message = "🤖 欢迎使用 Web3 投资提醒 Bot！\n\n指令示例：\n/start - 查看欢迎信息\n/next - 获取最新接力项目\n/strategy - 当前挂单策略\n\n📡 系统已接入 Telegram + Discord 联动提醒。"
    update.message.reply_text(welcome_message)
    
    # 同步推送到 Discord
    if DISCORD_WEBHOOK:
        try:
            requests.post(DISCORD_WEBHOOK, json={"content": f"📬 用户触发 /start：@{update.effective_user.username or '未知用户'}"})
        except Exception as e:
            logging.error(f"Discord 推送失败：{e}")

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # 注册指令
    dispatcher.add_handler(CommandHandler("start", start))

    # 启动 polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()