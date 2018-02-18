# Python 2.x Version
#from datetime import datetime, timedelta
#from dateutil import tz
#JST = tz.tzoffset('JST', 1 * 3600)
#local = tz.gettz() # Local time
#PT = tz.gettz('US/Pacific') # Pacific time

# Python 3.x Version
import datetime, pytz
from datetime import datetime as dt2, timedelta, timezone
JST = timezone(timedelta(hours=+9)) # Timezone

dt = dt2(2018, 2, 18, 21, 0, tzinfo=JST)
print(dt)

EZ = pytz.timezone('Europe/Zagreb') # Timezone Zagreb
dt_pst = dt2(2018, 1, 1, 12, tzinfo=EZ)
dt_pdt = dt2(2018, 7, 1, 12, tzinfo=EZ)  # DST is handled automatically
print(dt_pst)
print(dt_pdt)

# Date objext
today = datetime.date.today()
new_year = datetime.date(2019, 1, 1)
print(today)
print(new_year)

# Time objext
noon = datetime.time(12, 0, 0)
print(noon)

# Current datetime
now = datetime.datetime.now()
print(now)

# Datetime object
millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)
print(millenium_turn)