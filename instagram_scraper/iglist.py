import selenium, time, urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ask user for profile url to scrape
profileUrl = input("Enter profile url to scrape: ")

# Option to go headless (without opening chrome)
options = webdriver.ChromeOptions()
# open chrome and go to the set page
driver = webdriver.Chrome(options=options)

# set url of instagram page
driver.get(profileUrl)

last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust the delay as needed
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# find all links that match '/p/' and append to list named userPosts
userPosts = []
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        userPosts.append(post)

# close connections and chrome
driver.quit()

# Display the list of download URLs
for post in userPosts:
    print(post)
