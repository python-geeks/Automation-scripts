import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    # Add any necessary options like '--headless' here
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_generate_and_display_download_links(driver):
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

    for post in userPosts:
        print(post)  # Display the generated download URLs
