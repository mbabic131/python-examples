from datetime import datetime, timedelta
import pytz

PT = pytz.timezone('Europe/Zagreb')
dt_pst = PT.localize(datetime(2018, 1, 1, 12))
dt_pdt = PT.localize(datetime(2018, 11, 1, 0, 30))

print(dt_pst)
print(dt_pdt)

# Time between two date-times
a = datetime(2018, 1, 1, 12, 0, 0)
b = datetime(2018, 2, 18, 15, 0, 0)
print(a-b)
print((b-a).days)

# Datetime object to string
my_date = datetime(2018, 2, 15, 22, 0, 0)
date_string_format = '%b %d %Y, %H:%M:%S'
string_date = datetime.strftime(my_date, date_string_format)
print(string_date)

# String to datetime object
str_date = 'Feb 15 2018, 22:00:00'
obj_date = datetime.strptime(str_date, date_string_format)
print(obj_date)
