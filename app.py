from flask import Flask, request
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    message = update.message or update.edited_message

    if not message or not message.text:
        return "ok"

    text = message.text

    if text == "/start":
        message.reply_text("🤖 Bot 已上线！欢迎使用投资提醒系统。")
    elif text == "/simulate":
        message.reply_text("📊 模拟挂单收益功能已加载，请稍候分析结果。")
    elif text == "/exitplan":
        message.reply_text("🧠 组合挂单策略建议：将按当前 SOLX 持仓分 3 批次设定目标价。")
    elif text == "/cogni":
        message.reply_text("🧬 Cogni AI 项目监听中，TGE 时间待定，将自动提醒。")
    elif text == "/lightchain":
        message.reply_text("💡 Lightchain 状态追踪中，预计本周公布 Launch 信息。")
    elif text == "/ozak":
        message.reply_text("🎯 Ozak 项目追踪：已完成私募，等待 TGE。")
    elif text == "/adjust":
        message.reply_text("🔄 当前池子价格建议挂单区间为 $0.015 - $0.03。")
    elif text == "/status":
        message.reply_text("📈 当前监听状态：\n✅ Solaxy: 已启动挂单监听\n✅ Cogni: 已标记\n✅ Lightchain: 待上线提醒。")
    else:
        message.reply_text("🤖 指令未识别。请发送 /start 查看可用指令。")

    return "ok"

# 保留 app 实例作为入口
    
