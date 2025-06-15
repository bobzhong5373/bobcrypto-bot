import os

# 从环境变量中获取 Bot Token 和 Etherscan API Key
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY")

# 项目钱包监听地址（你自己的 Bitget 和 MetaMask 地址）
WATCHED_ADDRESSES = [
    "0x36175331c34d6C9459a9E56Fa54EB1ED58bbd7d6",  # Bitget 钱包
    "0x95FBEf31f758036AB2A579f36414fD39F40F0592",  # MetaMask 钱包
]

# 挂单监听目标价格（Solaxy 默认挂单）
ALERT_PRICES = [0.015, 0.02, 0.03]

# 支持的项目关键词（用于状态播报）
PROJECTS = {
    "solaxy": "Solaxy",
    "cogni": "Cogni AI",
    "ozak": "Ozak AI",
    "lightchain": "Lightchain AI"
}

# 支持的用户 ID，仅本人使用（你自己的 Telegram ID）
AUTHORIZED_USERS = [
    548765321  # ⚠️ 请替换为你自己的 Telegram ID
]

# 默认播报时间（每天早上 7:30 和晚上 20:30）
MORNING_TIME = "07:30"
EVENING_TIME = "20:30"

# 默认链（监听 ETH 链）
CHAIN = "ethereum"
