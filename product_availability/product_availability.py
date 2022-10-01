import requests
from bs4 import BeautifulSoup
import time
from send_email import send_email

HEADERS = ({'User-Agent':
            """Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36""",
            'Accept-Language': 'en-US, en;q=0.5'})


def product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features="html.parser")
    try:
        title = soup.find(id='productTitle').get_text().strip()
    except Exception as e:
        print(e)
        return None, None

    try:
        soup.select('#availability .a-color-success')[0].get_text().strip()
        available = True
    except Exception as e:
        print(e)
        available = False

    return title, available


if __name__ == '__main__':
    url = ""

    while True:
        print('checking...')
        time.sleep(1)
        title, available = product_info(url)
        print(title, available)
        if available:
            text = "Subject: Price Available Now!\n\n"
            text += "Your tracked products are Available Now!\n\n"
            text += f"{title}\n"
            text += f"{url}\n\n"
            if (send_email(text)):
                break
        else:
            print("Not Available")
