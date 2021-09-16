"""
This file can download slide share presentations on your local system without logging in :)
Steps to proceed ->
1). The url of the ppt is being provided
2). Using beautiful soup the tag section inside which the images of ppt are available  is scraped.
3). Scraped images are combined together using pyttx (forming a presentation)
"""
import requests
from bs4 import BeautifulSoup
from pptx import Presentation

url = 'https://www.slideshare.net/RajendraAkerkar/software-project-management-9146521'

data = requests.get(url)
my_data = []

html = BeautifulSoup(data.text, 'html.parser')
links = html.select('img.slide_image')

for link in links:
    image = link["data-full"]
    my_data.append(image)
print(len(my_data))
