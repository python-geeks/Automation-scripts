from datetime import datetime, timedelta
from dateutil import tz
import requests


def get_datetime(utc_time):
    utc = datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    return utc

def get_local_timestamp(utc, from_zone=None):
    
    if not from_zone:
        from_zone = tz.tzutc()

    to_zone = tz.tzlocal()  # Auto-detect zone

    """
    Tell the datetime object that it's in UTC time zone since 
    datetime objects are 'naive' by default
    """
    utc = utc.replace(tzinfo=from_zone)
    local_time = utc.astimezone(to_zone)    # Convert time zone
    
    return local_time

TOMORROW = get_local_timestamp((datetime.today() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0), from_zone=tz.tzlocal())
API_URL = "https://www.kontests.net/api/v1/all"

req = requests.get(API_URL)
data = req.json()

calendar = {}

for contest in data:

    local_start_time = get_local_timestamp(get_datetime(contest["start_time"])) 
    local_end_time = get_local_timestamp(get_datetime(contest["end_time"]))

    contest["start_time"] = local_start_time.strftime("%I:%M %p, %d %b '%y")
    contest["end_time"] = local_end_time.strftime("%I:%M %p, %d %b '%y")


    if local_end_time <= TOMORROW:  # If contest has already ended, skip
        continue
    elif local_start_time <= TOMORROW and local_end_time > TOMORROW:    # If contest is open today
        key="Today ({})".format(datetime.today().strftime("%d %b '%y"))
    else:   # Future contests
        key=local_start_time.strftime("%d %B, %Y")

    if key not in calendar:
        calendar[key] = [contest]
    else:
        calendar[key].append(contest)

for day, contests in calendar.items():
    print(f"\n\n{day}:")
    for contest in contests:
        print()
        print(f"\t{contest['name']} [{contest['site']}]")
        print(f"\t{contest['start_time']}  -  {contest['end_time']}")
        print(f"\tContest URL: {contest['url']}")

