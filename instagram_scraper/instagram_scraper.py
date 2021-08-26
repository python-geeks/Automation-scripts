# import selenium, time, urllib.request
from selenium import webdriver
import time
import urllib.request

profileUrl = input("enter profile url to scrape: ")
# open chrome and go to the set page
driver = webdriver.Chrome()
# set url of instagram page
driver.get(profileUrl)

# scroll to the bottom of the page
pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                   "var pageLength=document.body.scrollHeight;return pageLength;")
match = True
while match:
    lastCount = pageLength
    pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                       "var pageLength=document.body.scrollHeight;return pageLength;")
    if lastCount == pageLength:
        match = False

# find all links that match '/p' and append to list named userPosts
userPosts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        userPosts.append(post)


download_url = ''
# extract shortcode and identify post type, then download them as jpg or mp4 depending on post type
for post in userPosts:
    driver.get(post)
    shortcode = driver.current_url.split("/")[-2]
    postType = driver.find_element_by_xpath(
        '//meta[@property="og:type"]').get_attribute('content')
    if postType == 'video':
        download_url = driver.find_element_by_xpath(
            "//meta[@property='og:video']").get_attribute('content')
        urllib.request.urlretrieve(download_url, '{}.mp4'.format(shortcode))
    else:
        download_url = driver.find_element_by_xpath(
            "//meta[@property='og:image']").get_attribute('content')
        urllib.request.urlretrieve(download_url, '{}.jpg'.format(shortcode))
    time.sleep(5)
# close connections and chrome once all posts are downloaded
driver.close()
