from datetime import datetime
import pytz

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

# print "utcmoment_naive: {0}".format(utcmoment_naive) # python 2
print("utcmoment_naive: {0}".format(utcmoment_naive))
print("utcmoment:       {0}".format(utcmoment))

localFormat = "%Y-%m-%d %H:%M:%S"

timezones = ['America/Los_Angeles', 'Europe/Madrid', 'America/Puerto_Rico']

for tz in timezones:
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    print(localDatetime.strftime(localFormat))

# utcmoment_naive: 2017-05-11 17:43:30.802644
# utcmoment:       2017-05-11 17:43:30.802644+00:00
# 2017-05-11 10:43:30
# 2017-05-11 19:43:30
# 2017-05-11 13:43:30
