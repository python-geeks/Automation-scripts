'''
Import the necessary libraries
'''
# !pip install selenium
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup as soup

'''
Define the browser/driver and open the desired webpage
'''
driver = webdriver.Chrome(
    'D:\\Softwares\\chromedriver_win32\\chromedriver.exe'
)
driver.get('https://www.cardekho.com/filter/new-cars')
'''
Keep scrolling automatically and extract the data from the webpage and store it
'''
for i in range(0, 20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, \
    (document.body.scrollHeight)*0.73)")
    time.sleep(1)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
psoup = soup(res, "lxml")
containers = psoup.findAll(
    "div", {"gsc_col-md-12 gsc_col-sm-12 gsc_col-xs-12 append_list"}
)
cars = []
prices = []
engines = []
mileages = []
for i in containers:
    #     cars.append(i.div.img["alt"])
    price = i.findAll("div", {"class": "price"})
    q = price[0].text
    s = ""
    for h in q:
        if h != "*":
            s += h
        else:
            break
    prices.append(s)
    m = i.findAll("div", {"class": "dotlist"})
    f = m[0].findAll("span", {"title": "Mileage"})
    if len(f) != 0:
        mileages.append(f[0].text)
    else:
        mileages.append(" ")
    e = m[0].findAll("span", {"title": "Engine Displacement"})
    if len(e) != 0:
        engines.append(e[0].text)
    else:
        engines.append(" ")
df = pd.DataFrame(
    {
        'Car Name': cars,
        'Price': prices,
        'Engine': engines,
        'Mileage': mileages
    }
)
df.to_csv('carScrap.csv', index=False, encoding='utf-8')
