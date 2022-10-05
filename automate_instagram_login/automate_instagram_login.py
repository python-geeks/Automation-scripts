from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

name = input("Enter your username: ")
passW = input("Enter your password: ")

driver = webdriver.Chrome(executable_path="C://Users//Downloads//chromedriver.exe")

class InstaBot():
	def __init__(self, userName, passWord):
		self.userName = userName
		self.passWord = passWord

	def login(self):
		driver.get("https://www.instagram.com")

		elemUser = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
		elemUser.send_keys(self.userName)

		elemPass = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
		elemPass.send_keys(self.passWord)


ankur = InstaBot(name, passW)
ankur.login()