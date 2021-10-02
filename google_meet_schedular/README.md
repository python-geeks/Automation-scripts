# Google Meet Schedular

## 1. Installing all the dependencies
```
$ pip install requirements.txt
```
## 2. Setting up the driver 
- Check your Google Chrome version
- Download suitable driver for your device from [here](https://chromedriver.chromium.org/downloads) and extract it anywhere you like
- Now we add the path where you extracted into System Environment Variable
Note : In case of other browsers, please check for their respective drivers according to browser version and follow the same steps
## 3. Scheduling your meet
- Create a new Python file in the same directory as AutoMeet.py and code the following :
```
from AutoMeet import AutoMeet

auto = AutoMeet("email ID","password","link")
auto.automeetG()
```
- Replace email ID, password and link with your credentials and meeting link 
## Bonus1 (for a fixed schedule)
```
from AutoMeet import AutoMeet
import time
import datetime

getTime = str(datetime.datetime.today().time())
currentTime = getTime[:2] + getTime[3:5]
getDay = int(datetime.datetime.today().weekday())

times = [[1000, 1100], [1110, 1210], [1220, 1320]] #24hourformat
ack = [False,False,False]

usrname = "your_email_Id"
passwrd = "your_password"
LEC1 = "google meet link"
LEC2 = "google meet link"
LEC3 = "google meet link"

monday = [LEC1, LEC2, LEC3]
tuesday = [LEC2, LEC1, LEC3]
wednesday = [LEC1, LEC2, LEC3]
thursday = [LEC3, LEC1, LEC2]
friday = [LEC2, LEC3, LEC1]

days = [monday, tuesday, wednesday, thursday, friday]

while True:
    getTime = str(datetime.datetime.today().time())
    currentTime = int(getTime[:2] + getTime[3:5])

    day = days[getDay]
    for i in range(len(times)):
        if times[i][0] <= currentTime < times[i][1]:
            print(day[i])
            if not ack[i]:
                auto = AutoMeet(usrname,passwrd,"{}".format(day[i]))
                auto.automeetG()
                ack[i] = True

    print("HOLD")
    time.sleep(30)
```
## Bonus2 (get notified)
- Get notified of the url/links shared in your meet’s chatbox by opening terminal/CMD and enter :
```
$ notify-run register
```
- Scan the QR code in your phone and you will get the push notification
