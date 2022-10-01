import requests
import re
from bs4 import BeautifulSoup


# Gets top 250 movies from IMDB
def scrape_movies():

    response = requests.get('http://www.imdb.com/chart/top')
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]

    for i in range(len(movies)):
        movie_string = movies[i].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(i)) + 1:-7]
        print(("| " + str(i + 1)) + (" | " + movie_title) + (" | Rating : " + "{:.1f}".format(float(ratings[i]))))
    return


# Gets top 250 TV shows from IMDB
def scrape_tvshows():
    page = requests.get("https://www.imdb.com/chart/toptv")
    Results = re.findall(r'" alt="(.+?)".*?title="(.*?)".*?strong.*?"(.*?)"', page.text, re.DOTALL)
    for i in range(len(Results)):
        print("| " + str(i + 1) + " | " + Results[i][0] + " | Rating : " + Results[i][-1][:3])

    return


# USER INTERFACE

print("Type 'Movies' to get the Top 250 Movies on IMDB\n")
print("Type 'TV' to get the Top 250 TV Shows on IMDB\n")
print("Type 'exit' to exit\n")

val = input("Type here: ")
while (val):
    if val == 'Movies':
        globals()['scrape_movies']()
        print("\n")
        val = input("Type 'Movies' or 'TV' or 'exit': ")
    elif val == 'TV':
        globals()['scrape_tvshows']()
        print("\n")
        val = input("Type 'Movies' or 'TV' or 'exit': ")
    elif val == 'exit':
        val = ''
    else:
        val = input("Wrong Input. Try Again: ")
