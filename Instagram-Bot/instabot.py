from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
import random
import csv

already_follow = []

with open('follower.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if len(row) != 0:
            for element in row:
                already_follow.append(element)


class InstagramBot:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome("chromedriver.exe")

        self.username = username
        self.password = password

        self.browser.delete_all_cookies()
        self.browser.maximize_window()

    def wait_for_object(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_element_located((type, string)))

    def wait_for_objects(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_all_elements_located((type, string)))

    def login(self):
        self.browser.get("https://www.instagram.com")

        inputs = self.wait_for_objects(By.CSS_SELECTOR, '._2hvTZ.pexuQ.zyHYP')
        inputs[0].send_keys(self.username)
        inputs[1].send_keys(self.password)

        time.sleep(1)

        inputs[1].send_keys(Keys.ENTER)

        time.sleep(2)

    def follow_followers(self, root_name, number_follower):
        all_follower = []

        time.sleep(2)

        self.browser.get(f"https://www.instagram.com/{root_name}/")

        time.sleep(2)

        followers = self.wait_for_objects(By.CSS_SELECTOR, '._81NM2')
        followers[1].click()

        for i in range(1, number_follower + 1):
            time.sleep(2)
            src1 = self.wait_for_object(
                By.XPATH, f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')
            self.browser.execute_script("arguments[0].scrollIntoView();", src1)
            time.sleep(5)

            follower_name = src1.text.split()[0]

            if follower_name in already_follow:
                number_follower += 1
                continue
            else:
                all_follower.append(follower_name)

        with open('follower.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(all_follower)

        for follower in all_follower:
            self.browser.get(f"https://www.instagram.com/{follower}/")

            time.sleep(5)

            subscribe_buttons = self.wait_for_objects(
                By.XPATH, '//button[text()="Follow"]')
            subscribe_buttons[0].click()

            time.sleep(5)


bot = InstagramBot(username="enter-your-username-here", password="enter-your-password-here")
bot.login()
# bot.like_hashtag('lifestyle', 3)
bot.follow_followers("therock", 3)
