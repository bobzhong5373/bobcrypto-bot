from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
app = FastAPI()
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ 欢迎使用 BOBcryptoNotifier_bot！")

dispatcher.add_handler(CommandHandler("start", start))

@app.post("/")
async def process_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
    return {"status": "ok"}
