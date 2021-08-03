import schedule
import time
import os


print('Scheduler initialised')
schedule.every(1).day.do(lambda: os.system('python manage.py scrape'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)
