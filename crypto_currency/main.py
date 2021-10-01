# import required libraries
import requests
from bs4 import BeautifulSoup, NavigableString
from scrapy import Selector
import time
import csv
from selenium import webdriver
from tkinter import filedialog

print("For executing this program, you need a webdriver for your browser.....")
print(
    "Kindly download it and answer [y] if you have download and [n] if you didn't download."
)
confirm = input("Have you download the webdriver for your browser?")

# give options to the webdriver
if confirm == "y":
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--headless")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    file_path = filedialog.askopenfilename(
        initialdir="/downloads",
        title="Select Chrome Driver",
        filetype=[("Executable Files", "*.exe")],
    )

    if "chromedriver" in file_path:
        # initialize the webdriver
        driver = webdriver.Chrome(
            executable_path=r"{}".format(file_path), options=options
        )
    else:
        print("Select the chrome driver....")
        exit(1)
    # headers for the webdriver
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    # function to get the data in between tags

    def between(cur, end):
        while cur and cur != end:
            if isinstance(cur, NavigableString):
                text = cur.strip()
                if len(text):
                    yield text
            cur = cur.next_element

    # get_coins function to get the data from the website

    def get_coin():
        # store the data in a list
        allrows = []
        # get the data from the website
        r = requests.get(
            "https://coinmarketcap.com/coins/", headers=headers, verify=False
        )
        # parse the data
        soup = BeautifulSoup(r.text, "html.parser")

        sel = Selector(text=soup.prettify())

        # headings of the table
        columns = ["S.No", "Name", "Symbol", "URL"]
        allrows.append(columns)

        # get the data from the table
        cryptos = sel.xpath("//tr").extract()
        count = 1

        # iterate through the data
        for crypto in cryptos[1:]:
            soup = BeautifulSoup(crypto, features="html.parser")
            rows = soup.find_all("td")
            rows = [tr.text.strip() for tr in rows]
            rows[2] = list((rows[2].split("\n")))
            rows[2].pop(1)
            rows[2].pop(1)
            rows[2] = [tr.strip() for tr in rows[2]]
            for i in rows[2]:
                if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    rows[2].remove(i)
            while "" in rows[2]:
                rows[2].remove("")
            for i in rows[2]:
                if i == "Buy":
                    rows[2].remove(i)
            for a in soup.find_all("a", href=True, class_="cmc-link"):
                rows[2].append("https://coinmarketcap.com" + a["href"])
                break
            rows[2].insert(0, count)

            allrows.append(rows[2])

            count += 1

            # storing upto 100 coins
            if count == 101:
                break

        # write the data to a csv file
        with open("coins.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(allrows)

    # get_coin_data function to get the data of a coin from the website

    def get_coin_data(sym):
        # getting the data of a coin given in input
        with open("coins.csv", "r") as f:
            csv_reader = csv.reader(f, delimiter=",")
            row_num = 1

            csv_reader = list(csv_reader)
            for row in csv_reader:
                if len(row) == 0:
                    csv_reader.remove(row)
            for i in range(1, 51):
                if (sym.upper()) in csv_reader[i]:
                    row_num = i
                    break
        # opening the page of that coin
        driver.get(csv_reader[row_num][3])
        time.sleep(1.5)
        name = csv_reader[row_num][1]
        symbol = sym.upper()
        page_source = driver.page_source

        # parsing the data
        soup = BeautifulSoup(page_source, "html.parser")

        # getting the details of the coin given in that page
        rank_det = soup.find_all("div", class_="namePill")
        rank_det = [ele.text.strip() for ele in rank_det]
        rank_dets = rank_det[0].split()

        rank = rank_dets[1]
        watchlistcount = rank_det[2].split()
        watchlistcount = watchlistcount[1]

        circules = soup.find_all("div", class_="supplyBlockPercentage")
        circules = [circule.text.strip() for circule in circules]
        circulation_percentage = circules[0]

        prices = soup.find_all("div", class_="priceValue")
        prices = [prices.text.strip() for prices in prices]
        price = prices[0]

        marketcaps = soup.find_all("div", class_="statsValue")
        marketcaps = [marketcap.text.strip() for marketcap in marketcaps]
        valuebymarketcap = marketcaps[3]

        table = soup.find_all("td")
        tables1 = []
        for tab in table:
            tables = tab.find_all("span", class_="")
            tables1.append(tables)
        market_dominance = [ele.text.strip() for ele in tables1[5]][0]

        market_cap = [ele.text.strip() for ele in tables1[7]][0]

        athl = soup.find_all("small", class_="hhPSEo")
        athl = [ele.text.strip() for ele in athl]
        ath_date = athl[0][:12]
        atl_date = athl[1][:12]

        ath_price = [ele.text.strip() for ele in tables1[17]][0]
        atl_price = [ele.text.strip() for ele in tables1[18]][0]

        whatiscoin = " ".join(
            text
            for text in between(
                soup.find(
                    "h2", text="What Is {} ({})?".format(name, symbol)
                ).next_sibling,
                soup.find("h3", text="Who Are the Founders of {}?".format(name)),
            )
        )

        foundcoin = " ".join(
            text
            for text in between(
                soup.find(
                    "h3", text="Who Are the Founders of {}?".format(name)
                ).next_sibling,
                soup.find("h4", text="What Makes {} Unique?".format(name)),
            )
        )

        uniqueness = " ".join(
            text
            for text in between(
                soup.find("h4", text="What Makes {} Unique?".format(name)).next_sibling,
                soup.find(id="related-pages"),
            )
        )

        listlinks = soup.find_all("a", class_="modalLink")
        listlinks = [ele["href"] for ele in listlinks]
        website_url = listlinks[0]

        headers1 = [
            "Symbol",
            "Name",
            "WatchlistCount",
            "Website",
            "Circulation %",
            "Price",
            "Value by market cap",
            "Market Dominance",
            "Rank",
            "Market Cap",
            "All time high date",
            "All time high price",
            "All time lowest date",
            "All time lowest price",
            "What is {}?".format(name),
            "Who are the founders of {}?".format(name),
            "What makes {} unique?".format(name),
        ]
        res_arr = [
            symbol,
            name,
            watchlistcount,
            website_url,
            circulation_percentage,
            price,
            valuebymarketcap,
            market_dominance,
            rank,
            market_cap,
            ath_date,
            ath_price,
            atl_date,
            atl_price,
            whatiscoin,
            foundcoin,
            uniqueness,
        ]

        # writing the data to a csv file
        with open(
            "coin_data_{}.csv".format(
                str(time.strftime("%b-%d-%Y_%H%M", time.localtime()))
            ),
            "w",
        ) as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers1)
            csvwriter.writerow(res_arr)

    # Calling the functions
    get_coin()
    get_coin_data(input("Enter the symbol of the coin: "))

else:
    print("Kindly download the webdriver to execute this code.")
