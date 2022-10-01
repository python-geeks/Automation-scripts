from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.webdriver.chrome.options import Options


def findMySong(song_name):
    '''
        function which accepts string and returns list of 10 available songs
    '''
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("http://mp3clan.top/mp3/")

    search_box = driver.find_elements_by_xpath('.//*[@id="search-orange"]')
    search_box[0].send_keys(song_name)
    search_box[0].click()

    button = driver.find_element_by_class_name("searchClan-button-left")
    button.click()

    time.sleep(10)

    try:
        songs = driver.find_elements_by_class_name('mp3list-table')
        song_list = []
        cnt = 0
        for song in songs:
            try:
                if (cnt < 10):
                    details = song.find_element_by_class_name(
                        "mp3list-play").text
                    details = details.split("\n")
                    link_sel_obj = song.find_element_by_tag_name("a")
                    link = link_sel_obj.get_attribute("href")
                    link = link[:33] + "get" + link[37:]
                    if (len(details) > 2):
                        vid_item = {
                            'title': details[0],
                            "duration": details[-1],
                            "download-link": link
                        }
                        song_list.append(vid_item)
                        cnt += 1
                else:
                    break
            except NoSuchElementException:
                print("no files found")
                continue
    except NoSuchElementException:
        print("big error")
    driver.close()
    return (song_list)


def downloadMySong(url):
    '''
        function which accepts url,
        and download's and save song in current directory
    '''
    try:
        options = Options()
        options.headless = True

        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        driver.set_page_load_timeout(20)

        driver.get(url)
        driver.get(url)

        time.sleep(10)
        driver.close()
    except TimeoutException:
        print("session timeout")
        driver.close()
