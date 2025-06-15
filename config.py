import os

# Telegram Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Etherscan API Key（用于链上监听）
ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY")

# 默认监听地址（可替换为你自己的钱包地址或项目地址）
WATCHED_ADDRESSES = [
    "0x36175331c34d6C9459a9E56Fa54EB1ED58bbd7d6",  # 你的 Bitget 钱包
    "0x95FBEf31f758036AB2A579f36414fD39F40F0592",  # 你的 MetaMask 钱包
    # 可添加更多地址
]

# 价格提醒配置（代币合约地址 => 目标价格）
PRICE_ALERTS = {
    "SOLX": {
        "symbol": "SOLX",
        "contract": "0x0000000000000000000000000000000000000000",  # 替换为真实合约地址
        "thresholds": [0.015, 0.02, 0.03]
    }
}

# 推送接收人 Telegram ID（只限你本人）
AUTHORIZED_USER_ID = 555555555  # 替换为你的 Telegram ID（可用 /getid Bot 获取）
