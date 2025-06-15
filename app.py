from flask import Flask, request
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    message = update.message
    text = message.text if message else ""

    if text == "/start":
        message.reply_text("🤖 Bot 已上线！欢迎使用投资提醒系统。")
    elif text == "/simulate":
        message.reply_text("📊 模拟挂单收益功能即将启动…")
    elif text == "/exitplan":
        message.reply_text("🧠 组合挂单策略建议模块已激活…")
    elif text == "/cogni":
        message.reply_text("🍬 Cogni AI 项目监听已启用。")
    elif text == "/lightchain":
        message.reply_text("💡 Lightchain 状态更新已同步。")
    elif text == "/ozak":
        message.reply_text("🎌 Ozak 项目追踪：正在监听 TGE 时间与动态。")
    elif text == "/adjust":
        message.reply_text("🔄 当前池子价格建议挂单区间将在策略更新后推送。")
    elif text == "/status":
        message.reply_text("📈 当前监听状态：\n✅ Solaxy: 已启动挂单监听\n✅ Lightchain: 等待 TGE\n✅ 巨鲸追踪: 待绑定 /bind")
    else:
        message.reply_text("🤖 指令未识别。请发送 /start 查看欢迎信息")

    return "ok"
