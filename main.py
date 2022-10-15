import schedule
import datetime
from health import report


def job():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    print(f'现在是: {time}')
    report('GH7376', '123456')


schedule.every(1).day.at('07:00').do(job)
schedule.every(1).day.at('12:30').do(job)

while True:
    schedule.run_pending()
