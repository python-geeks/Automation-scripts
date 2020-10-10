#!/usr/bin/env python3
import requests
import bs4

def getPrice(URL):

    country_prefix = ""

    if "amazon.de" in URL:
        country_prefix = "de."
        URL = URL.replace("/dp/", "/product/")

    URL = URL.replace("?", "/")
    ProductID = URL.split("/product/", 1)[1].split("/")[0]

    headers = {
        'authority': 'www.camelcamelcamel.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    htmldata = requests.get("https://" + country_prefix + "camelcamelcamel.com/product/" + ProductID, headers=headers)
    soup = bs4.BeautifulSoup(htmldata.text, 'html.parser')
    current = ".".join(soup.find("span", {'class': 'green'}).text[:-1].split(","))
    highest  = ".".join(soup.find("tr", {'class': 'highest_price'}).text.strip().split("\n")[1][:-1].split(","))
    lowest = ".".join(soup.find("tr", {'class': 'lowest_price'}).text.strip().split("\n")[1][:-1].split(","))
    return (float(current), float(highest), float(lowest))
    # try:
    #     #return soup.find("span", {'class': 'green'}).text
    # except:
    #     pass

print(getPrice("https://www.amazon.de/dp/B07R4MYTF6?tag=camelcamelc06-21&linkCode=ogi&th=1&psc=1&language=de_DE"))