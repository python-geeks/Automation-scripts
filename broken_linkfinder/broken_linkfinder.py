import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

searched_links = []
broken_links = []


def getLinksFromHTML(html):
    def getLink(el):
        return el["href"]
    return list(map(getLink, BeautifulSoup(html, features="html.parser").select("a[href]")))


def find_broken_links(domainToSearch, URL, parentURL):
    if (not (URL in searched_links)) and (not URL.startswith("mailto:")) and (not ("javascript:" in URL)) and \
            (not URL.endswith(".png")) and (not URL.endswith(".jpg")) and (not URL.endswith(".jpeg")):
        try:
            requestObj = requests.get(URL)
            searched_links.append(URL)
            if(requestObj.status_code == 404):
                broken_links.append("BROKEN: link " + URL + " from " + parentURL)
                print(broken_links[-1])
            else:
                # comment this line if you want to print only broken links
                print("NOT BROKEN: link " + URL + " from " + parentURL)
                if urlparse(URL).netloc == domainToSearch:
                    for link in getLinksFromHTML(requestObj.text):
                        find_broken_links(domainToSearch, urljoin(URL, link), URL)
        except Exception as e:
            print("ERROR: " + str(e))
            searched_links.append(domainToSearch)


find_broken_links(urlparse(sys.argv[1]).netloc, sys.argv[1], "")

print("\n--- DONE! ---\n")
print("The following links were broken:")

for link in broken_links:
    print("\t" + link)
