from apscheduler.schedulers.blocking import BlockingScheduler
from run_daily import run

scheduler = BlockingScheduler()
scheduler.add_job(run, 'cron', hour=8, minute=0)  # 北京时间早上8点
scheduler.start()
