from apscheduler.schedulers.blocking import BlockingScheduler
from app.email_sender import send_mail
from zoneinfo import ZoneInfo

scheduler = BlockingScheduler(timezone = ZoneInfo("Asia/Kolkata"))

scheduler.add_job(
    send_mail,
    trigger='cron',
    hour = 9,
    minute = 0
)
print("Scheduler started....")

scheduler.start()