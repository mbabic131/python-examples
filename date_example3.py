import datetime, time
from datetime import datetime as dt1

today = datetime.date.today()
print('Today:', today)

yesterday = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)

tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)

seconds_since_epoch = time.time()
print(seconds_since_epoch)

utc_date = dt1.utcfromtimestamp(seconds_since_epoch)
print(utc_date)
