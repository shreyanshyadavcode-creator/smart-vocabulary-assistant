from apscheduler.schedulers.blocking import BlockingScheduler
import os

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.resend_sender_module import send_mail
from zoneinfo import ZoneInfo

def safe_send():

    try:
        print("Running scheduled task...")
        send_mail()
        print("Task completed successfully")

    except Exception as e:
        print("Scheduler Error:", e)


scheduler = BlockingScheduler(
    timezone=ZoneInfo("Asia/Kolkata")
)
scheduler.add_job(
    safe_send,
    trigger="interval",
    
    hours=9,

    minutes=0
)

print("Scheduler started...")

scheduler.start()