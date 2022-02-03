from selenium import webdriver
from time import sleep

mail= input("Enter your mail:")
password = input("Enter your password")

chromepath="C:/Users/bhavi/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chromepath)

driver.get('https://teams.microsoft.com')
driver.implicitly_wait(5)

driver.find_element_by_id("i0116").send_keys(mail)

driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input").click()
sleep(2)

driver.find_element_by_id("i0118").send_keys(password)
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()

sleep(2)

driver.find_element_by_xpath("/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input").click()
sleep(2)
driver.find_element_by_id("app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c").click()
sleep(2)
driver.find_element_by_xpath('//*[@title="Join"]').click()