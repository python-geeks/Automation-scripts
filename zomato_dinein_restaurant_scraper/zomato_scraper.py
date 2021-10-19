# -- IMPORTING LIBRARIES --
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time


# -- STARTING CHROME WITH WEBDRIVER --
browser = webdriver.Chrome()


# -- OPENING URL IN BROWSER --
url = 'https://www.zomato.com/indore/dine-out'
browser.get(url)


# -- ITERATING THROUGH THE PAGE TO GET ALL THE RESTAURANTS --
for i in range(0, 25):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight*0.81);")
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight*0.86);")
    time.sleep(1)

# -- EXTRACTING PAGE SOURCE --
html = browser.page_source

# -- CREATING BeautifulSoup OBJECT --
soup = BeautifulSoup(html, 'html.parser')


# -- DEFINING FUNCTION FOR EXTRACTING RESATURANT DETAILS --
def zomato(soup):
    name = [i.text.strip() for i in soup.find_all('h4', class_='sc-1hp8d8a-0 sc-dpiBDp iFpvOr')]
    cuisine = [i.text.strip() for i in soup.find_all('p', class_='sc-1hez2tp-0 sc-hENMEE ffqcCI')]
    area = [i.text.strip() for i in soup.find_all('p', class_='sc-1hez2tp-0 sc-dCaJBF jughZz')]
    rate = [i.text.strip() for i in soup.find_all('p', class_='sc-1hez2tp-0 sc-hENMEE crfqyB')]
    return pd.DataFrame({'Name': name, 'Cuisine': cuisine, 'Area': area, 'Rate for Two': rate})


# -- DISPLAYING AND EXPORTING RESULTS --
df = zomato(soup)
print(df.head())
df.to_csv('Zomato Restaurants.csv')
