import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
from selenium.common.exceptions import TimeoutException

@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    # Add any necessary options like '--headless' here
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_scrape_and_download_limited_posts(driver):
    profileUrl = 'https://www.instagram.com/iamandrewcarroll/'  # Replace with a valid profile URL

    driver.get(profileUrl)

    max_scroll_attempts = 2
    scroll_delay = 15
    scroll_timeout = 30

    # Simulate scrolling by executing JavaScript to scroll the page
    for _ in range(max_scroll_attempts):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_delay)
        except TimeoutException:
            # If TimeoutException occurs during scrolling, attempt to reload the page
            print("Timeout occurred during scrolling. Attempting to reload the page.")
            driver.refresh()
            time.sleep(scroll_delay)

    userPosts = []
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        post = link.get_attribute('href')
        if '/p/' in post:
            userPosts.append(post)

    # Directory in which to save the files
    download_dir = os.path.join(os.getcwd(), 'downloads')

    # Create a WebDriverWait instance with a timeout for further interactions
    wait = WebDriverWait(driver, scroll_timeout)  # Adjust the timeout as needed

    for post in userPosts:
        driver.get(post)
        shortcode = driver.current_url.split("/")[-2]

        try:
            # Wait for the presence of the post type element
            postType_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '//meta[@property="og:type" and @content="video"] | //meta[@property="og:type" and @content="image"]'))
            )
            postType = postType_element.get_attribute('content')

            if postType in ['video', 'image']:
                # Wait for the visibility of the post type element
                postType_element = wait.until(EC.visibility_of(postType_element))
                if postType_element:
                    meta_property = 'og:video' if postType == 'video' else 'og:image'
                    file_extension = 'mp4' if postType == 'video' else 'jpg'

                    # Retrieve download URL and save the file
                    download_url = driver.find_element(By.XPATH, f"//meta[@property='og:{meta_property}']").get_attribute('content')
                    file_path = os.path.join(download_dir, f'{shortcode}.{file_extension}')
                    urllib.request.urlretrieve(download_url, file_path)
                    assert os.path.exists(file_path)

                    # If it's a video, wait for the video to finish playing
                    if postType == 'video':
                        video_element = driver.find_element(By.TAG_NAME, 'video')
                        video_duration = float(video_element.get_attribute('duration'))
                        time.sleep(video_duration)
                        
            time.sleep(5)
        except TimeoutException:
            print(f"Timeout occurred for post: {post}")
