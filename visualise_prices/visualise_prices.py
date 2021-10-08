from nsetools import Nse
import requests
from datetime import datetime as dt, timedelta
import plotly.graph_objects as go
import pandas as pd

nse = Nse()
headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                  (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    "Sec-Fetch-User": "?1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, \
               image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
}


def fetch_data(stock, start_date, end_date):
    series = "EQ"
    start_date = start_date.strftime("%d-%m-%Y")
    end_date = end_date.strftime("%d-%m-%Y")

    url = (
        "https://www.nseindia.com/api/historical/cm/equity?symbol="
        + stock
        + "&series=[%22"
        + series
        + "%22]&from="
        + str(start_date)
        + "&to="
        + str(end_date)
        + ""
    )
    try:
        data = requests.get(url, headers=headers).json()
    except ValueError:
        s = requests.Session()
        data = s.get("http://nseindia.com", headers=headers)
        data = s.get(url, headers=headers).json()
    return pd.DataFrame.from_records(data["data"])


def visualise_stock(symbol):

    if not nse.is_valid_code(symbol):
        raise ValueError("Not a Valid Stock Tick")

    symbol = symbol.upper()
    end_date = dt.now()
    start_date = end_date - timedelta(days=365)
    limit = 50  # Request return 50 entries at a time
    size = timedelta(days=limit)
    data = pd.DataFrame()

    while start_date < end_date:
        data = data.append(
            fetch_data(symbol, start_date, min(end_date, start_date + size))
        )
        start_date = start_date + size

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data["CH_TIMESTAMP"],
                open=data["CH_OPENING_PRICE"],
                high=data["CH_TRADE_HIGH_PRICE"],
                low=data["CH_TRADE_LOW_PRICE"],
                close=data["CH_CLOSING_PRICE"],
            )
        ],
        layout={
            "title": {
                "text": nse.get_stock_codes()[symbol],
                "xanchor": "center",
                "x": 0.5,
            },
            "yaxis": {
                "title": {
                    "text": "Stock Price",
                }
            },
        },
    )

    fig.show()


if __name__ == "__main__":
    visualise_stock(input("Enter the stock tick: "))
