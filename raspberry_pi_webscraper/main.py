import requests
from bs4 import BeautifulSoup

def scrape_adafruit():
    url = "https://www.adafruit.com/product/4295"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    options = soup.find(class_="meta_pid_boxes").find_all("a")
    print("--- Adafruit ---")
    for option in options:
        status = option.find(class_="meta_pid_box_status").get_text().lower()
        ram_size = option.find(class_="stripes_oos_tag").get_text().strip()
        if "in" in status:
            print(ram_size, "is available -", url)
    print()


def scrape_pishop_us():
    urls = {
        "1gb": "https://www.pishop.us/product/raspberry-pi-4-model-b-1gb/",
        "2gb": "https://www.pishop.us/product/raspberry-pi-4-model-b-2gb/",
        "4gb": "https://www.pishop.us/product/raspberry-pi-4-model-b-4gb/",
        "8gb": "https://www.pishop.us/product/raspberry-pi-4-model-b-8gb/",
    }
    print("--- PiShop US ---")
    for ram_size, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        status = soup.find(id="form-action-addToCart")["value"].lower()
        if "in" in status:
            print(ram_size, "is available -", url)
    print()


def scrape_vilros():
    urls = {
        "1gb": "https://vilros.com/products/raspberry-pi-4-model-b",
        "2gb": "https://vilros.com/collections/raspberry-pi/products/raspberry-pi-4-2gb-ram",
        "4gb": "https://vilros.com/collections/raspberry-pi/products/raspberry-pi-4-4gb-ram",
        "8gb": "https://vilros.com/collections/raspberry-pi/products/raspberry-pi-4-model-b-8gb-ram",
    }
    print("--- Vilros ---")
    for ram_size, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        status = (
            soup.select("span[data-add-to-cart-text]")[0].get_text().strip().lower()
        )
        if "out" not in status:
            print(ram_size, "is available -", url)
    print()


def scrape_chicago_electronics():
    urls = {
        "1gb": "https://chicagodist.com/products/raspberry-pi-4-model-b-1gb",
        "2gb": "https://chicagodist.com/products/raspberry-pi-4-model-b-2gb",
        "4gb": "https://chicagodist.com/products/raspberry-pi-4-model-b-4gb",
        "8gb": "https://chicagodist.com/products/raspberry-pi-4-model-b-8gb",
    }
    print("--- Chicago Electronic Distributors ---")
    for ram_size, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        status = soup.find(class_="modal_price").find("span").get_text().strip().lower()
        if "out" not in status:
            print(ram_size, "is available -", url)
    print()


def scrape_okdo():
    urls = {
        "2gb": "https://www.okdo.com/us/p/raspberry-pi-4-model-b-2gb-2/"
    }
    print("--- OKdo ---")
    for ram_size, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        status = soup.find(class_="c-stock-level").get_text().strip().lower()
        if "out" not in status:
            print(ram_size, "is available -", url)
    print()


def scrape_canakit():
    urls = {
        "1gb": "https://www.canakit.com/raspberry-pi-4.html",
        "2gb": "https://www.canakit.com/raspberry-pi-4-2gb.html",
        "4gb": "https://www.canakit.com/raspberry-pi-4-4gb.html",
        "8gb": "https://www.canakit.com/raspberry-pi-4-8gb.html",
    }
    print("--- Canakit ---")
    for ram_size, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        status = (
            soup.find(id="ProductAddToCartDiv").find("span").get_text().strip().lower()
        )
        if "out" not in status:
            print(ram_size, "is available -", url)
    print()


def main():
    scrape_adafruit()
    scrape_pishop_us()
    scrape_vilros()
    scrape_chicago_electronics()
    scrape_okdo()
    scrape_canakit()


if __name__ == "__main__":
    main()
