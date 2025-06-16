from fastapi import FastAPI, Request
import os
import telebot

# 从环境变量获取 Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# 创建 FastAPI 实例
app = FastAPI()

# 设置 Webhook 接收路径
@app.post("/")
async def telegram_webhook(request: Request):
    json_data = await request.body()
    update = telebot.types.Update.de_json(json_data.decode("utf-8"))
    bot.process_new_updates([update])
    return {"status": "ok"}

# 定义 /start 指令
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🤖 你好，我是你的 Web3 投资助手 BOBcryptoNotifier_bot！\n\n你可以发送 /status 查看监听状态，或 /next 获取今日推荐项目。")

# 可在本地测试运行时添加：
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app:app", host="0.0.0.0", port=8080)
