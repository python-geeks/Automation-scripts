import pandas as pd
import webbrowser
import pyautogui
import time
# Reading the file
import datetime
import calendar


def findDay(tdate):
    born = datetime.datetime.strptime(tdate, '%Y-%m-%d').weekday()
    return calendar.day_name[born]


tdate = datetime.date.today()

# printing todays date

print('Current date: ', tdate)

d = findDay(str(tdate))
print(d)
df = pd.read_csv(str(d) + '.csv')

# Starting the session


def sign_in(url):

    # url = 'https://meetingsapac15.webex.com/meet/ddpuri'
    try:
        path = 'C://Program Files//Google//Chrome//Application//chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
        webbrowser.get('chrome').open(url)
    except path.DoesNotExist:
        path = 'C://Program Files(x86)//Google//Chrome//Application//chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
        webbrowser.get('chrome').open(url)
    time.sleep(20)
    print('we are here')
    meeting_id_btn = 'NONE'
    while meeting_id_btn == 'NONE':
        meeting_id_btn = pyautogui.locateCenterOnScreen('1.png')
        print(meeting_id_btn)
        pyautogui.moveTo(meeting_id_btn)
        pyautogui.click()


def sign_out():

    import wmi
    ti = 0
    name = ['CiscoCollabHost.exe', 'webexmta.exe', 'atmgr.exe']
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name in name:
            process.Terminate()
            ti += 1
            break
    if ti == 0:
        print('Process not found!!!')


while True:

    # checking of the current time exists in the csv file

    now = datetime.now().strftime('%H:%M')
    if now in str(df['timings']):

        row = df.loc[df['timings'] == now]
        url = str(row.iloc[0, 1])

        sign_in(url)
        print('signed in')

    if now in str(df['end']):
        row = df.loc[df['end'] == now]
        sign_out()

        print('signed out')
