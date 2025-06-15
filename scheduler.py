import schedule
import time
import threading

from broadcast import morning_broadcast, evening_broadcast
from monitors import check_price, check_whale_activity

def run_schedule():
    # 每日早上 7:30 播报
    schedule.every().day.at("07:30").do(morning_broadcast)
    # 每日晚上 20:30 播报
    schedule.every().day.at("20:30").do(evening_broadcast)
    # 每 5 分钟检查一次价格
    schedule.every(5).minutes.do(check_price)
    # 每 5 分钟检查一次鲸鱼动态
    schedule.every(5).minutes.do(check_whale_activity)

    while True:
        schedule.run_pending()
        time.sleep(1)

# 用于后台线程启动
def start_scheduler():
    thread = threading.Thread(target=run_schedule)
    thread.daemon = True
    thread.start()
