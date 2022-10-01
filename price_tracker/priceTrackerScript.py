import requests
from bs4 import BeautifulSoup
import unicodedata
import time
from send_email import send_email


HEADERS = ({'User-Agent':
            """Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like
            Gecko) Chrome/41.0.2228.0 Safari/537.36""",
            'Accept-Language': 'en-US, en;q=0.5'})


def get_product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features="html.parser")
    try:
        title = soup.find(id='productTitle').get_text().strip()
        price_str = soup.find(id="priceblock_ourprice").get_text()
    except Exception as e:
        print(e)
        return None, None, None

    try:
        soup.select('#availability .a-color-success')[0].get_text().strip()
        available = True
    except Exception as e:
        print(e)
        available = False

    try:
        price = unicodedata.normalize("NFKD", price_str)
        price = price.replace(',', '').replace('₹', '')
        price = float(price)

    except Exception as e:
        print(e)
        return None, None, None

    return title, price, available


def createTuple(urls, limits):
    if len(urls) != len(limits):
        print("""url list and limit list are not equal
        --Make Sure you add "," after each url and limit""")
        return []
    return [(urls[i], limits[i]) for i in range(0, len(urls))]


if __name__ == '__main__':
    urls = [
        # Add URL of Amazon Website here as shown below
        "url1",
        "url2"
    ]
    limits = [
        # Add crossponding limit to which you want to get email
        # like you want get email when price below 100 so put 100 in the limit
        "limit1",
        "limit2"
    ]

    products = createTuple(urls, limits)
    while True:
        if (len(products) == 0):
            break
        print('Number of products left whose price is Not Dropped yet',
              len(products))
        print('checking...')
        time.sleep(10)
        products_below_limit = []
        for product_url, limit in products:
            title, price, available = get_product_info(product_url)
            if title is not None and price < limit and available:
                products_below_limit.append((product_url, title, price, limit))
        if products_below_limit:
            message = "Subject: Price below limit!\n\n"
            message += "Your tracked products are below the given limit!\n\n"
            foundData = []
            for url, title, price, limit in products_below_limit:
                message += f"{title}\n"
                message += f"Price: {price}\n"
                message += f"{url}\n\n"
                foundData.append((url, limit))

            if (send_email(message)):
                for found in foundData:
                    products.remove(found)
