import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

# Flask 应用初始化
app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0)

# /start 指令
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 欢迎使用 BOBcrypto 投资提醒机器人！支持以下命令：\n\n"
                              "/next - 查看接力推荐项目\n"
                              "/claim - Solaxy Claim 状态\n"
                              "/price - 当前挂单价格说明\n"
                              "/strategy - 当前策略模板")

# /next 指令
def next(update: Update, context: CallbackContext):
    update.message.reply_text("📢 今日推荐接力项目：\n\n"
                              "名称：Lightchain AI\n"
                              "类型：ZK + AI\n"
                              "TGE：预计 3 日内\n"
                              "募资上限：300,000 USDT\n"
                              "初始流通：极低\n"
                              "上线：MEXC 专属通道\n\n"
                              "👉 风险控制良好，适合 Solaxy 套现后接力布局。")

# /claim 指令
def claim(update: Update, context: CallbackContext):
    update.message.reply_text("📦 Solaxy 目前尚未开放 Claim。\n\n"
                              "预计 Claim 开启时间：6 月 16 日 21:30（UTC+8）\n"
                              "请保持关注，系统将通过 Telegram 自动提醒。")

# /price 指令
def price(update: Update, context: CallbackContext):
    update.message.reply_text("💰 当前监听挂单价格区间：\n\n"
                              "🔹 0.015 USDT（保本提醒）\n"
                              "🔹 0.02 USDT（第一目标）\n"
                              "🔹 0.03 USDT（高抛目标）\n\n"
                              "系统将自动监控 Uniswap 实时价格并提醒突破。")

# /strategy 指令
def strategy(update: Update, context: CallbackContext):
    update.message.reply_text("📊 当前 Solaxy 分批挂单策略：\n\n"
                              "1. 40% 挂 0.02 USDT\n"
                              "2. 40% 挂 0.025 USDT\n"
                              "3. 20% 挂 0.03 USDT\n\n"
                              "开盘后可根据价格表现实时调整挂单。")

# 添加指令处理器
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("next", next))
dispatcher.add_handler(CommandHandler("claim", claim))
dispatcher.add_handler(CommandHandler("price", price))
dispatcher.add_handler(CommandHandler("strategy", strategy))

# Webhook 路由
@app.route('/', methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# 心跳测试用（可选）
@app.route('/', methods=["GET"])
def index():
    return "Bot is running!"

# 仅用于 Railway 部署
if __name__ == "__main__":
    app.run(debug=True, port=5000)
