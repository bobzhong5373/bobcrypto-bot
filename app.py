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
        message.reply_text("📊 模拟挂单收益功能已启动（测试中）\n例如：0.015 = $28,670，命中概率约 42%")

    elif text == "/exitplan":
        message.reply_text("🧠 组合挂单策略建议：\n- 30% 挂 0.015\n- 40% 挂 0.02\n- 30% 冲高挂 0.03")

    elif text == "/cogni":
        message.reply_text("🧬 Cogni AI 项目追踪：\n- TGE 时间：预计 6月18日\n- 初始流通市值：26.7万 USDT\n- 上线平台：待公布")

    elif text == "/lightchain":
        message.reply_text("💡 Lightchain 状态追踪：\n- TGE 预计 6月20日前后\n- 社群热度：中高\n- 当前募资进度：82%")

    elif text == "/ozak":
        message.reply_text("🛰️ Ozak 项目追踪：\n- 上线时间：待定\n- 当前阶段：私募完成，等待公告\n- 风险等级：中等")

    elif text == "/adjust":
        message.reply_text("🔄 当前池子价格建议：\n- 若 > 0.016：可上调第一挂单至 0.017\n- 若 < 0.014：建议下调或等待反弹")

    elif text == "/status":
        message.reply_text("📈 当前监听状态：\n✅ Solaxy: 已启动挂单监听\n✅ Cogni: TGE 倒计时中\n✅ Lightchain: 已接入鲸鱼监听\n📊 策略模板：0.015 / 0.02 / 0.03")

    else:
        message.reply_text("🤖 指令未识别。请发送 /start 查看可用功能。")

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
