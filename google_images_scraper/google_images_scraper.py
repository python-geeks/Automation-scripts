from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import argparse
import os
import driver_downloader


def image_search_scrape():
    if os.path.isfile("/usr/bin/geckodriver"):
        pass
    else:
        driver_downloader.driver_download()
    # taking user arguments
    parser = argparse.ArgumentParser(description="Scrape Google images")
    parser.add_argument(
        "-s", "--search", default="", type=str, help="search term"
    )
    parser.add_argument(
        "-d", "--directory", default="/images", type=str, help="save directory"
    )
    parser.add_argument(
        "-iC", "image_count", default="100", type=int, help="Number of images to dowmload"
    )
    args = parser.parse_args()
    query = args.search
    savePath = args.directory
    numImages = args.image_count
    print("Search Term is " + query)
    print("Images will be saved to this " + savePath + " directory")
    site = "https://www.google.com/search?tbm=isch&q=" + query
    # providing driver path (usually in /usr/bin/geckodriver) if not 
    # then current dir (check line 13)
    driver = webdriver.Firefox(executable_path=".")
    # passing site url
    driver.get(site)
    '''
    the below scrapes only the first instance of the search, no scrolling.
    '''    
    if numImages <=15:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    
    else:
    """
    below while loop scrolls the webpage 5 times(if available, also scrolling beyond 
    that the results get a bit diluted)
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
        except Exception as e:
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
        except Exception as e:
            pass
    print("Total images downloaded = " + count)


if __name__ == "__main__":
    image_search_scrape()
