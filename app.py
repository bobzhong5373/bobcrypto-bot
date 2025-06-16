from fastapi import FastAPI, Request
import telebot
import os

# 从环境变量获取 Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# 创建 FastAPI 应用对象，供 Uvicorn 引用
app = FastAPI()

# Webhook 接收接口
@app.post("/")
async def telegram_webhook(request: Request):
    body = await request.body()
    update = telebot.types.Update.de_json(body.decode("utf-8"))
    bot.process_new_updates([update])
    return "ok"

# 指令：/start
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.reply_to(message, "✅ 欢迎使用 BOBcryptoNotifier_bot\n\n你可以输入 /status 查看当前监听状态，或 /next 查看今日推荐项目。")
