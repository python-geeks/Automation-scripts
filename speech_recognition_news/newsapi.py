import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
from newspaper import Article
from newspaper import Config
from datetime import datetime

news_information = dict()

failed_port_connection = []

now = datetime.now()
todays_date = now.strftime("%b %d, %Y")


def get_top_news(news_information, todays_date):
    load_dotenv(find_dotenv(r"path to env variable"))
    news_api_key = os.getenv("news_api")
    params = (
        ('country', 'us'),
        ('apiKey', f'{news_api_key}'),
    )
    response = requests.get(
        """https://newsapi.org/v2/top-headlines""",
        params=params)
    news_articles = response.json()['articles']
    for i in news_articles:
        user_agent = """Mozilla/5.0 (Macintosh;
        Intel Mac OS X 10.15; rv:78.0)
        Gecko/20100101 Firefox/78.0"""
        config = Config()
        config.browser_user_agent = user_agent
        config.request_timeout = 10
        article = Article(i['url'], config=config)
        print(i["url"])
        article.download()
        article.parse()
        article.nlp()
        summary = article.summary  # noqa
        news_information[i["source"]["name"]] = {"title": i["title"], "summary": summary, "url": i["url"], "date": f"{todays_date}"}  # noqa


def json_file(news_information, todays_date):
    json_file = json.dumps(news_information, indent=4)
    with open(f"news_summary/news_summary {todays_date}.txt", "w") as outfile:
        outfile.write(json_file)
        outfile.close()
