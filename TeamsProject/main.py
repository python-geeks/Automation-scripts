import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import yaml
import sys
import time
import pyautogui as magic
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from datetime import datetime



sys.tracebacklimit=0


settings_path="D:\Desktop\Python Documents\TeamsProject\settings.yaml"
with open(settings_path) as f:
    settings = yaml.load(f, Loader=yaml.FullLoader)


logindetails = settings['logindetails']
username = logindetails['username']
password = logindetails['password']

mon= settings['monday']
tue= settings['tuesday']
wed= settings['wednesday']
thur= settings['thursday']
fri= settings['friday']

def initiation():
    print("Class starting..")
    print("Initiating Bot!")
    print("Starting Teams")
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver= webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=options)
    driver.get("https://teams.microsoft.com")
    driver.maximize_window()
    usernameentry()
    time.sleep(1)
    passentry()
    time.sleep(1)
    findingcal()
    time.sleep(1)
    findingactivejoinbutton()
    time.sleep(1)
    allow()
    time.sleep(1)
    finaljoin()
    time.sleep(1)
    waitingforendtime()

def checkingforday():
    sys.setrecursionlimit(10**9)
    date = datetime.now()
    week_num= datetime.date(date).weekday()
    week_days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    todayday= week_days[week_num]
    global timingstart
    global timingend
    if todayday== "Monday":
        timingstart= mon['starttimings']
        timingend= mon['endtimings']
    elif todayday== "Tuesday":
        timingstart= tue['starttimings']
        timingend= tue['endtimings']
    elif todayday== "Wednesday":
        timingstart= wed['starttimings']
        timingend= wed['endtimings']
    elif todayday== "Thursday":
        timingstart= thur['starttimings']
        timingend= thur['endtimings']
    elif todayday== "Friday":
        timingstart= fri['starttimings']
        timingend= fri['endtimings']
    print("Today is a ", todayday)
    waitingforstarttime()

def waitingforstarttime():
    print("Waiting for the class to start.")
    while True:
        curr = datetime.now().strftime("%H:%M")
        for now in timingstart:
            if now==curr:
                initiation()
                
def waitingforendtime():
    print("Class Joined! Waiting for class to end!")
    while True:
        curr = datetime.now().strftime("%H:%M")
        for now in timingend:
            if now==curr:
                meetingend()

def meetingend():
    driver.find_element_by_id("hangup-button").click()
    driver.close()
    checkingforday()


def usernameentry():
    time.sleep(1)
    try:
        driver.find_element_by_id("i0116").send_keys(username)
    except selenium.common.exceptions.NoSuchElementException:
        usernameentry()
    magic.press('enter')

def passentry():
    time.sleep(1)
    try:
        driver.find_element_by_id("i0118").send_keys(password)
    except selenium.common.exceptions.NoSuchElementException:
        passentry()
    time.sleep(1)
    magic.press('enter')
    remembersignin()
    
def remembersignin():   
    findwindow= magic.locateCenterOnScreen("D:\Desktop\Python Documents\TeamsProject\core\staysignedin.png")
    if findwindow== None:
        remembersignin()
    else:
        magic.press('enter')


def findingcal():
    time.sleep(1)
    try:
        driver.find_element_by_id("app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c").click()
    except selenium.common.exceptions.NoSuchElementException:
        findingcal()

def findingactivejoinbutton():
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@title="Join"]').click()
    except selenium.common.exceptions.NoSuchElementException:
        findingactivejoinbutton()

def allow():
    perm= magic.locateCenterOnScreen('D:\Desktop\Python Documents\TeamsProject\core\llow.png')
    if perm==None:
        allow()
    else:
        magic.moveTo(perm)
        magic.click()

def finaljoin():
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@title="Turn camera off"]').click()
    except selenium.common.exceptions.NoSuchElementException:
        finaljoin()
    driver.find_element_by_xpath('//*[@title="Mute microphone"]').click()
    driver.find_element_by_class_name("button-col").click()


checkingforday()