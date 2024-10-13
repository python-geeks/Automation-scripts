import argparse
from datetime import datetime
import pytz

def timezone(timezone_1):
    zones = pytz.all_timezones
    

    if timezone_1 in zones :
        timezone = pytz.timezone(timezone_1)
        time = datetime.now(timezone)
        print("Current Time in ",timezone_1,"is=",time)
    else :
        print("The zone provided is not correct")

if __name__=="__main__":
    inputs=argparse.ArgumentParser()
    inputs.add_argument('-t','--time',type=str, help='Timezone', required=True)
    value=inputs.parse_args().time
    timezone(value)
  