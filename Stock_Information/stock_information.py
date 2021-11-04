import praw
import os
import nltk
import re
import sqlite3
import yfinance as yf
from collections import Counter
from dotenv import load_dotenv, find_dotenv
from praw.models import MoreComments

load_dotenv(find_dotenv(r"path to environmental variable"))

Reddit = praw.Reddit(
    client_id=os.getenv("reddit_key"),
    client_secret=os.getenv("reddit_secret"),
    user_agent=os.getenv("user_agent"),
    username=os.getenv("reddit_username"),
    password=os.getenv("reddit_pasword"))

wsb_subreddit = Reddit.subreddit("wallstreetbets")

countered_dict = {}

top_ticker_symbols = []


def get_stock_information(countered_dict):
    top_5 = sorted(countered_dict, key=countered_dict.get, reverse=True)[:5]
    for ticker in top_5:
        ticker_info = yf.Ticker(ticker)
        company_name = ticker_info.info['shortName']
        conn = sqlite3.connect("stock_info.db")
        ticker_table = conn.cursor()
        ticker_table.execute(""""CREATE TABLE IF NOT EXISTS Stock_information
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Company_name TEXT,
            Sector TEXT,
            Stock_Price,
            Symbol TEXT,
            Total_Revenue INTEGER
            );
            """)
        sql_company = ticker_table.execute(f"""
        SELECT * FROM Stock_information
        WHERE Company_name = '{company_name}
        '""")
        Company_check = sql_company.fetchall()
        length_check = [i for i in Company_check]
        if ticker_info.info["quoteType"] == "ETF":
            sector = "No sector/ETF"
            price = ticker_info.info["previousClose"]
            total_revenue = "N/A"
        else:
            sector = ticker_info.info["sector"]
            price = ticker_info.info["currentPrice"]
            total_revenue = ticker_info.info["totalRevenue"]
        if len(length_check) > 0:
            ticker_table.execute(f"""
            UPDATE Stock_information
            SET Stock_Price = {price}
            WHERE Symbol = '{ticker_info.info['symbol']}';
            """)
        else:
            ticker_table.execute("""INSERT INTO Stock_information
            (
            Company_name,
            Sector, Stock_Price,
            Symbol, Total_Revenue
            )
            VALUES (?, ?, ?, ?, ?
            );""", (
                ticker_info.info["shortName"],
                sector, price,
                ticker_info.info["symbol"],
                total_revenue)
                )
        conn.commit()


def top_wallstreebet_stocks(top_ticker_symbols):
    Nouns = lambda pos: pos[:2] == "NN"
    pattern = r'[A-Z]+\b'
    for submissions in wsb_subreddit.hot(limit=5):
        for top_level_comment in submissions.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            stock_tickers = nltk.word_tokenize(top_level_comment.body)
            stock_ticker_list = list(set([
                word
                for (word, pos) in nltk.pos_tag(stock_tickers)
                if Nouns(pos) and
                re.findall(pattern, word) and
                len(yf.Ticker(word).info) > 10 and not
                word.startswith("/u/")
                ]))
            top_ticker_symbols = top_ticker_symbols + stock_ticker_list
    countered_dict = dict(Counter(top_ticker_symbols))
    get_stock_information(countered_dict)

