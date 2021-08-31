import subprocess
import pyautogui
import time
import pandas as pd
# Reading the file
import datetime
import calendar

def findDay(tdate):
	born = datetime.datetime.strptime(tdate, '%Y-%m-%d').weekday()
	return (calendar.day_name[born])





from datetime import date
tdate = date.today()

# printing todays date
print("Current date: ", tdate)

d=findDay(str(tdate))
print(d)
df = pd.read_csv(str(d)+'.csv')
from datetime import datetime

#Starting the session
def sign_in(url):
    import webbrowser

    #url = 'https://meetingsapac15.webex.com/meet/ddpuri'
    try:
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    except:
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files(x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    import pyautogui
    import time
    time.sleep(20)
    print("we are here")
    meeting_id_btn="NONE"
    while meeting_id_btn=="NONE":
        meeting_id_btn =  pyautogui.locateCenterOnScreen('1.png')
        print(meeting_id_btn)
        pyautogui.moveTo(meeting_id_btn)
        pyautogui.click()
    """
    try:
        pyautogui.click(1135, 900)
    except:
        spyautogui.click(1135,1100)
    time.sleep(2)
    """
def sign_out():
    
    import wmi
    ti = 0
    name = ['CiscoCollabHost.exe','webexmta.exe','atmgr.exe']
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name in name:
            process.Terminate()
            ti += 1
            break
    if ti == 0:
        print("Process not found!!!")


while True:
    # checking of the current time exists in the csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       url= str(row.iloc[0,1])

       sign_in(url)
       time.sleep(40)
       print('signed in')

    if now in str(df['end']):
        row = df.loc[df['end'] == now]
        sign_out()
        #time.sleep(20)
        print('signed out')
