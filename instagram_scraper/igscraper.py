import selenium, time, urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlretrieve
import os

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

# set up WebDriverWait for waiting for elements
wait = WebDriverWait(driver, 10) # Adjust the timeout as needed

# download_url = ''
# extract shortcode and identify post type, then download them as jpg or mp4 depending on post type
for post in userPosts:
    driver.get(post)
    shortcode = driver.current_url.split("/")[-2]
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//meta[@property="og:type"]')))
    postType = element.get_attribute('content')

    if postType in ['video', 'image']:
        meta_property = 'og:video' if postType == 'video' else 'og:image'
        file_extension = 'mp4' if postType == 'video' else 'jpg'

        download_url = driver.find_element(By.XPATH, f"//meta[@property='og:{meta_property}']").get_attribute('content')
        # urllib.request.urlretrieve(download_url, os.path.join(os.getcwd(), 'downloads', shortcode + '.' + file_extension))
        urllib.request.urlretrieve(download_url, 'downloads' + shortcode + '.' + file_extension)


    time.sleep(5)
# close connections and chrome once all posts are downloaded
driver.close()
