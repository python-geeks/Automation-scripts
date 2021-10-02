from selenium import webdriver
import time
import re
# from pynput.keyboard import Controller
from notify_run import Notify


class AutoMeet():
    usernameStr = None
    passwordStr = None
    url_meet = None
    options = None
    browser = None

    def __init__(self, username_string, password_string, url_of_meet,):
        self.usernameStr = username_string
        self.passwordStr = password_string
        self.url_meet = url_of_meet
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--window-size=800,600")
        self.options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.media_stream_mic": 2,
            # "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2
        })
        self.browser = webdriver.Chrome(chrome_options=self.options)

    # ---------------Wrapper for Gmail ID And Non Gmail ID-----------------
    def automeetG(self):
        self.browser.get(('https://stackoverflow.com/'))
        # self.browser.find_element_by_xpath("/html/body/header/div/ol[2]/li[2]/a[2]").click()
        self.waiting_N_click("/html/body/header/div/ol[2]/li[2]/a[2]")
        # self.browser.find_element_by_xpath("//*[@id=\"openid-buttons\"]/button[1]").click()
        self.waiting_N_click("//*[@id=\"openid-buttons\"]/button[1]")
        username = self.browser.find_element_by_id('identifierId')
        username.send_keys(self.usernameStr)
        nextButton = self.browser.find_element_by_id('identifierNext')
        nextButton.click()
        time.sleep(15)  # 5
        # keyboard = Controller()
        # keyboard.type(passwordStr)
        password = self.browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        password.send_keys(self.passwordStr)
        # keyboard.type(passwordStr)
        signInButton = self.browser.find_element_by_id('passwordNext')
        signInButton.click()
        time.sleep(5)  # 3
        self.browser.get(self.url_meet)
        time.sleep(10)  # 6
        element = self.browser.find_element_by_class_name('Ce1Y1c')
        self.browser.execute_script("arguments[0].click();", element)
        try:
            self.browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div').click()
            try:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), \
                                                    'Ask to join')]").click()
            except BaseException:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), \
                                                    'Join now')]").click()
        except BaseException:
            try:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), \
                                                    'Ask to join')]").click()
            except BaseException:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), \
                                                    'Join now')]").click()
        # time.sleep(15) # Wasnt here
        # self.browser.find_element_by_xpath("//*[@id=\"ow3\"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span").click()
        self.waiting_N_click("//*[@id=\"ow3\"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span")
        currentStudents = 0
        greatestStudents = 0
        text_temp = ""
        final_text = ""
        while True:
            time.sleep(25)  # reduce it later
            text = self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/ \
                                                      div/div[2]/div[2]/div[2]/span[2]/div/div[1]").text
            people = self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[3]/ \
                                                      div/div[2]/div[2]/div[1]/div[1]").text
            # print(people)
            # print(text)
            final_text = text.replace(text_temp, "")
            # print(final_text)
            text_temp = text
            link = re.findall(r"(http|ftp|https)://([\w-]+(?:(?:.[\w-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",
                              final_text)
            if ("http" in final_text):
                notify = Notify()
                notify.send(link[0][0] + "://" + link[0][1], link[0][0] + "://" + link[0][1])
                print(link[0][0] + "://" + link[0][1])
            people_int = re.findall(r'[0-9]+', people)
            # print(people_int[0])
            currentStudents = int(people_int[0])
            if currentStudents > greatestStudents:
                greatestStudents = currentStudents
            else:
                if currentStudents < greatestStudents / 2:
                    self.browser.close()
                    break

    def waiting_N_click(self, path):
        try:
            self.browser.find_element_by_xpath(path).click()
        except BaseException:
            # print("1")
            time.sleep(2)
            self.waiting_N_click(path)
