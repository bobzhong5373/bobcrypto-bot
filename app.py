import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler
import requests
from flask import Flask

# 环境变量
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# 初始化 Telegram Bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# 启动 Flask 保活（Render 保活策略）
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!", 200

# Telegram 指令响应逻辑
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ 已启动 Web3 Bot 系统")

def next_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="📌 当前接力项目：\n1. Cogni AI\n2. Lightchain AI")

def claim(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🎯 当前状态：Solaxy 未开启 Claim")

def strategy(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="📈 当前挂单策略：\n1. 25% 挂 0.015\n2. 40% 挂 0.02\n3. 剩余挂 0.03")

def price(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="💡 当前池子价格监听中...\n设定提醒价：0.015 / 0.02 / 0.03")

def simulate(update, context):
    test_text = "✅ 测试播报：Solaxy 项目即将 Claim，请准备挂单操作"
    context.bot.send_message(chat_id=update.effective_chat.id, text=test_text)
    if DISCORD_WEBHOOK:
        try:
            requests.post(DISCORD_WEBHOOK, json={"content": test_text})
        except Exception as e:
            print(f"❌ Discord webhook failed: {e}")

# 启动 polling 保活模式
def run_bot():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("next", next_command))
    dispatcher.add_handler(CommandHandler("claim", claim))
    dispatcher.add_handler(CommandHandler("strategy", strategy))
    dispatcher.add_handler(CommandHandler("price", price))
    dispatcher.add_handler(CommandHandler("simulate", simulate))

    updater.start_polling()
    print("✅ Bot polling started")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_bot()
    app.run(host="0.0.0.0", port=10000)