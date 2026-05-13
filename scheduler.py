from apscheduler.schedulers.blocking import BlockingScheduler
from app.gmail_sender_module import send_mail
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
    seconds = 300

    # hour=9,

    # minute=0
)

print("Scheduler started...")

scheduler.start()