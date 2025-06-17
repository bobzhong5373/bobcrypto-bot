import telebot
import requests
import os

# 从环境变量中读取配置
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ✅ Telegram Bot 启动测试指令
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "🤖 你好，我是你的 Web3 投资提醒机器人！\n\n📌 支持以下功能：\n- Solaxy 挂单提醒\n- Claim 启动监控\n- Discord 联动推送\n\n请输入 /next 获取今日推荐项目。"
    bot.reply_to(message, welcome_text)
    # 同步推送至 Discord
    send_to_discord(f"🟢 Telegram 用户启动了 Bot：{message.chat.id} 已发送 /start")

# ✅ 示例命令 /next：推荐今日项目
@bot.message_handler(commands=['next'])
def send_next(message):
    text = "📌 今日推荐项目：\n1. Cogni AI（TGE 待定）\n2. Lightchain AI（关注 ZK 落地）\n3. Ozak AI（具备题材叙事）"
    bot.reply_to(message, text)
    send_to_discord("📢 /next 命令触发：已返回今日项目推荐")

# ✅ 推送内容到 Discord Webhook
def send_to_discord(content):
    if DISCORD_WEBHOOK:
        try:
            requests.post(DISCORD_WEBHOOK, json={"content": content})
        except Exception as e:
            print(f"[❌ Discord 推送失败] {e}")

# ✅ 启动 Bot 轮询模式（适用于 Render）
if __name__ == "__main__":
    print("🤖 Bot 正在启动中…")
    bot.polling(non_stop=True)