from bs4 import BeautifulSoup
import requests


# get top stories from The Associated Press website


def get_soup(url):
    resp = requests.get(url, 
                        headers={'User-Agent': 'Mozilla/5.5 (Windows NT 12.1)'})
    soup = BeautifulSoup(resp.text, 'html5lib')
    return soup


def main():
    url = "https://www.apnews.com"
    
    soup = get_soup(url)
    
    news_items = soup.find_all("div", attrs={'data-key': 'related-story'})

    print('{} Top Stories on {}'.format(len(news_items), url))
    
    for item in news_items:
        link = item.find('a').get('href')
        print(url + link)
        headline = item.find('div', attrs={'data-key': 'related-story-headline'})
        timestamp = item.find('span', attrs={'data-key': 'timestamp'})
        print(timestamp.text)
        print(headline.text)
        print('*' * 20)


if __name__ == '__main__':
    main()