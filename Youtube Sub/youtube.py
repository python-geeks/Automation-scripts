from selenium import webdriver

open=webdriver.Chrome()
open.get('https://youtube.com')

searchmenu=open.find_element_by_xpath('//*[@id="search"]')
searchmenu.send_keys('Pewdiepie')

go=open.find_element_by_xpath('//*[@id="search-icon-legacy"]')
go.click()