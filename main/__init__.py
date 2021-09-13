import subprocess

from apscheduler.schedulers.blocking import BlockingScheduler


def some_job():
    subprocess.call(['ls', '-la'])
    # subprocess.call(['cat','~/.gitconfig'])
    subprocess.call(['git', 'config', '--global', 'user.name', '"shreyakishore"'])
    subprocess.call(['git', 'config', '--global', 'user.email', '"shreyakishore5@gmail.com"'])
    subprocess.call(['git', 'config', '--global', 'user.password', '"AnuradhaKass5"'])
    # subprocess.call(['cat', 'gitpush.sh'])
    # subprocess.call(['sh', './gitpush.sh'])
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-m', '"auto push"'])
    subprocess.call(['git', 'push', 'origin', 'master'])


scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=10)
scheduler.start()
