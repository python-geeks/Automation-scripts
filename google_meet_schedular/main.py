from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import date,datetime
import calendar
import schedule
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.alert import Alert
from time import sleep
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from os import system

def Glogin(email, psswd,code,driver):
    driver.get("https://meet.google.com/new")
    search = driver.find_element_by_name("identifier")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    search = driver.find_element_by_name("password")
    print(search)
    search.send_keys(psswd)
    search.send_keys(Keys.RETURN)
    sleep(3)
    driver.get("https://meet.google.com/lookup/" + code)
    sleep(3)

def turnOffMicCam(driver):
    time.sleep(2)
    button = driver.find_element_by_class_name("sUZ4id")
    button.click()
    driver.implicitly_wait(3000)
    time.sleep(1)
    button = driver.find_element_by_class_name("GOH7Zb")
    button.click()
    driver.implicitly_wait(3000)

def joinNow(driver):
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

def leave(driver):
    button = driver.find_element_by_class_name("s1GInc.zCbbgf")
    button.click()
    driver.quit()
def mainlink():
    driver=cre()
    code= "deiumbxrex"
    Glogin(email, psswd,code,driver)
    turnOffMicCam(driver)
    joinNow(driver)
    time.sleep(3000)
    try:
        leave(driver)
    except:
        print("you already left")
def sllink():
    driver=cre()
    code= "pxibpxqedo"
    Glogin(email, psswd,code,driver)
    turnOffMicCam(driver)
    joinNow(driver)
    time.sleep(3000)
    try:
        leave(driver)
    except:
        print("you already left")
def tplink():
    driver=cre()
    code="qgkmsfbphn"
    Glogin(email, psswd,code,driver)
    turnOffMicCam(driver)
    joinNow(driver)
    time.sleep(3000)
    try:
        leave(driver)
    except:
        print("you already left")
def iotlink():
    driver=cre()
    code="tdixgbdmxf"
    Glogin(email, psswd,code,driver)
    turnOffMicCam(driver)
    joinNow(driver)
    time.sleep(3000)
    try:
        leave(driver)
    except:
        print("you already left")
email = "18b61a05d6@nmrec.edu.in"
psswd = "nmrec123"
def cre():

    path = "chromedriver.exe"
    opt = Options()
    opt.add_argument("start-maximized")
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
    })

    driver = webdriver.Chrome(executable_path=path,chrome_options=opt)
    return driver

schedule.every().monday.at("09:30").do(mainlink)
schedule.every().monday.at("11:20").do(mainlink)
schedule.every().monday.at("12:12").do(mainlink)
schedule.every().monday.at("13:03").do(mainlink)

schedule.every().tuesday.at("09:30").do(iotlink)
schedule.every().tuesday.at("10:22").do(mainlink)
schedule.every().tuesday.at("11:23").do(mainlink)
schedule.every().tuesday.at("12:14").do(mainlink)

schedule.every().wednesday.at("09:30").do(iotlink)
schedule.every().wednesday.at("10:22").do(sllink)
schedule.every().wednesday.at("11:22").do(tplink)
schedule.every().wednesday.at("12:12").do(tplink)
schedule.every().wednesday.at("13:02").do(mainlink)

schedule.every().thursday.at("09:30").do(iotlink)
schedule.every().thursday.at("10:22").do(mainlink)
schedule.every().thursday.at("11:22").do(mainlink)
schedule.every().thursday.at("12:12").do(mainlink)
schedule.every().thursday.at("13:02").do(sllink)

schedule.every().friday.at("09:30").do(mainlink)
schedule.every().friday.at("11:20").do(sllink)
schedule.every().friday.at("12:10").do(mainlink)
schedule.every().friday.at("13:00").do(mainlink)

schedule.every().saturday.at("09:30").do(sllink)
schedule.every().saturday.at("10:20").do(mainlink)
schedule.every().saturday.at("11:20").do(mainlink)
schedule.every().saturday.at("12:10").do(mainlink)
schedule.every().saturday.at("13:00").do(mainlink)

while True:
    schedule.run_pending()
