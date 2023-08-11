import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from scrapfly import ScrapflyClient, ScrapeApiResponse, ScrapeConfig

SCRAPFLY = ScrapflyClient(os.getenv('SCRAPFLY_KEY'))  # Load your Scrapfly API key from environment variable

def scrape_and_download_limited_posts(profile_url: str, download_dir: str) -> None:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.get(profile_url)

    max_scroll_attempts = 2
    scroll_delay = 15
    scroll_timeout = 60

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

    wait = WebDriverWait(driver, scroll_timeout)

    for post in userPosts:
        driver.get(post)
        shortcode = driver.current_url.split("/")[-2]

        try:
            postType_element = wait.until(
                EC.presence_of_element_located((By.XPATH, '//meta[@property="og:type" and @content="video"] | //meta[@property="og:type" and @content="image"]'))
            )
            postType = postType_element.get_attribute('content')

            if postType in ['video', 'image']:
                postType_element = wait.until(EC.visibility_of(postType_element))
                if postType_element:
                    meta_property = 'og:video' if postType == 'video' else 'og:image'
                    file_extension = 'mp4' if postType == 'video' else 'jpg'

                    download_url = driver.find_element(By.XPATH, f"//meta[@property='og:{meta_property}']").get_attribute('content')

                    # Create a unique filename for the downloaded file
                    file_name = f'{shortcode}.{file_extension}'
                    file_path = os.path.join(download_dir, file_name)

                    # Use Scrapfly to download the file ethically
                    response = SCRAPFLY.scrape(ScrapeConfig(download_url))
                    if response.status_code == 200:
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                    else:
                        print(f"Failed to download file: {download_url}")

            # No wait time for video posts
            if postType != 'video':
                time.sleep(5)
        except TimeoutException:
            print(f"Timeout occurred for post: {post}")

    driver.close()

if __name__ == "__main__":
    # Prompt the user to enter the URL to scrape
    profile_url = input("Enter the Instagram profile URL to scrape: ")
    download_directory = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    scrape_and_download_limited_posts(profile_url, download_directory)
