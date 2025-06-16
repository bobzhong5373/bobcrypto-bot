from fastapi import FastAPI, Request
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = FastAPI()

# 监听 Telegram Webhook 的主路由
@app.post("/")
async def webhook(request: Request):
    body = await request.body()
    update = telebot.types.Update.de_json(body.decode("utf-8"))
    bot.process_new_updates([update])
    return "ok"

# 注册 /start 指令
@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.reply_to(message, "✅ 你好！系统已连接 BOBcryptoNotifier_bot 成功～\n\n📊 你可以输入 /status 查询策略执行状态。\n🧠 或输入 /next 获取今日推荐项目。")
