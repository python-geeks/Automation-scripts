import requests
import csv
import sys
from bs4 import BeautifulSoup as bs


def main():
    # Base url for the latest articles on the hackernews website
    baseurl = "https://news.ycombinator.com/newest"

    # Number of articles requested by the user
    try:
        number_of_articles = int(input(
            '''Enter the number of articles you want from the hackernews website.
(1-30) : '''))
    except ValueError:
        print("\nYou did not enter a number. Try again.\n")
        sys.exit(1)

    if not 1 <= number_of_articles <= 30:
        print("\nYour input was not in the given range!\n")
        sys.exit(1)
    # Response obect to fetch the hackernews url
    response = requests.get(baseurl)

    # soup object for easy scrapping
    soup = bs(response.content, 'html.parser')

    # Finding all the a tags with the class storylink
    latest = soup.find_all('a', attrs={'class': 'storylink'})

    # list to track the links of the articles
    links = []

    # list to keep track of the names of the articles
    titles = []

    # Fetching the links and names from the soup object
    # storing them in respective lists
    for article in latest:
        links.append(article['href'])
        titles.append(article.text)

    result = []

    for title, link in zip(titles[:number_of_articles],
                           links[:number_of_articles]):
        d = {}
        d["News Title"] = title
        d["Link to the News"] = link
        result.append(d)

    keys = ["News Title", "Link to the News"]

    with open("hackernews_latest.csv", "w") as hackernews:
        writer = csv.DictWriter(hackernews, fieldnames=keys)
        writer.writeheader()
        writer.writerows(result)

    return


if __name__ == "__main__":
    main()
    print("\nYour news file has been successfully created!\n")
