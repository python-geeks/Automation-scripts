from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time
import argparse
import os

import geckodriver_autoinstaller


def driver_download():
    # Check if the current version of geckodriver exists
    # if it doesn't exist, download it automatically,
    # then add geckodriver to PATH.
    geckodriver_autoinstaller.install()


def google_images_scraper():
    GECKO_PATH = "/path/to/gecko/dir"  # /usr/bin/geckodriver
    if os.path.isfile(GECKO_PATH):
        pass
    else:
        driver_download()
    # taking user arguments
    parser = argparse.ArgumentParser(description="Scrape Google images")
    parser.add_argument(
        "-s", "--search", default="mangoes", type=str, help="search term"
    )
    parser.add_argument(
        "-d", "--directory", default="images/", type=str, help="save directory"
    )
    args = parser.parse_args()
    query = args.search
    savePath = args.directory
    print("Search Term is " + query)
    print("Images will be saved to " + savePath + " directory")
    site = "https://www.google.com/search?tbm=isch&q=" + query
    # providing driver path
    driver = webdriver.Firefox(executable_path=GECKO_PATH)
    # passing site url
    driver.get(site)
    """
    if you just want to download 10-15 images then skip the while loop and
    just write
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    below while loop scrolls the webpage 5 times(if available,
    also scrolling beyond that the results get a bit diluted)
    (will be able to retrieve around 250-300 images)
    """
    i = 0
    while i < 5:
        # for scrolling page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        try:
            # for clicking show more results button
            driver.find_element_by_xpath(
                "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input"
            ).click()

        except Exception:
            pass
        time.sleep(5)
        i += 1

    # parsing
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # closing web browser
    driver.close()
    # scraping image urls with the help of image tag and class used for images
    imgTags = soup.find_all("img", class_="rg_i")
    count = 0
    for i in imgTags:

        try:
            # passing image urls one by one and downloading
            urllib.request.urlretrieve(i["src"], savePath + str(count) + ".jpg")
            count += 1
            print("Number of images downloaded = " + str(count), end="\r")

        except Exception:
            pass
    print("Total images downloaded = " + str(count))


if __name__ == "__main__":
    google_images_scraper()
