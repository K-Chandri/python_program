from datetime import date

today_date = date.today()
print(today_date)

from datetime import datetime
 
time_now = datetime.now().strftime('%H:%M:%S')
print(f'the time now is{time_now}')