# import selenium, time
from selenium import webdriver
import time


# open chrome and go to the set page
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/funnywhimsical/")


# scroll to the bottom of the page
pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                   "var pageLength=document.body.scrollHeight;return pageLength;")
match = False
while(match == False):
    lastCount = pageLength
    time.sleep(2)
    pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                       "var pageLength=document.body.scrollHeight;return pageLength;")
    if lastCount == pageLength:
        match = True