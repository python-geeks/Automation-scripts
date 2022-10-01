from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

name = ["Bot"]
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https:// web.whatsapp.com/ ")
bot = "Hi"
time.sleep(8)
a = "//*[@id='side']/div[1]/div/label/div/div[2]"
search_box = driver.find_element_by_xpath(a)
search_box.send_keys(name)
search_box.send_keys(Keys.ENTER)
for a in range(1, 43):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(8)
lastmsg = driver.find_elements_by_class_name("cvjcv _1Ilru")
msg = driver.find_elements_by_class_name("_1Gy50")
print("There was issue while tracing the last test!,Try again \n")
driver.quit()
driver.get("https://web.whatsapp.com/")
msg = msg[-1]
msg_1 = msg.text
msg_1 = msg_1.split("\n")
print("The last message \n", msg_1)
print("There was an issue while login!, Try again \n")
text_box = driver.find_element_by_xpath(
    '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]'
)
text = 'From Bot: "{}" \n'.format(bot)
text_box.send_keys(text + Keys.ENTER)
"""driver.quit()"""
print("Done! \n")
print("There's an issue while sending a message!,Try again \n")
driver.quit()
