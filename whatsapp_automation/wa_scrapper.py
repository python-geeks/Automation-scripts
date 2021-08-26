from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

 
name=['Bot']  #initializing the person/group name 
driver=webdriver.Chrome(executable_path="whatsapp_automation\chromedriver.exe") #mention the path of the chromedriver's executable (present in the folder)
driver.get("https://web.whatsapp.com/") #mentioned the official link of whatsapp

bot="Hi" #initialized the text to be sent
time.sleep(8) #given a definite time to wait and load the screen (You can change it)
search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]') #path of the search box present at the left
search_box.send_keys(name) #types in the name ("Bot" mentioned in the list name )
search_box.send_keys(Keys.ENTER) # searches and clicks on the name found

try:
    for i in range(1,43):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scrolls to the end of the page to get the last message
    time.sleep(8) #again a break for 8 seconds to load
    try:
        lastmsg = driver.find_elements_by_class_name('cvjcv _1Ilru') #class name of the last text (main div)
        msg = driver.find_elements_by_class_name('_1Gy50') #class name of the last text (text div)
    except:
        print("There was issue while tracing the last test!, Try again")
        driver.quit()
        driver.get("https://web.whatsapp.com/")
    msg = msg[-1] 
    msg_1 = msg.text #print the text only
    msg_1 = msg_1.split('\n')
    print(msg_1)   

except:
    print("There was an issue while login!, Try again")
    driver.quit()

try:
    text_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]') #searches the text box
    text='From Bot: "{}"'.format(bot) #types in the text 
    text_box.send_keys(text+ Keys.ENTER) #send the message
    driver.quit() #will quit the chromepage automatically
    print('Done!')
except:
    print("There's an issue while sending a message!, Try again")
    driver.quit()