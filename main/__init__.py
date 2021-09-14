import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler


def some_job():
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-m', '"auto push"'])
    subprocess.call(['git', 'push', 'origin', 'master', '--force'])

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=10)
scheduler.start()
