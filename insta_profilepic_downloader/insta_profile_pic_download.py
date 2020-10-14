# import the required libraries
# install these using the command "pip install -r requirements.txt"
# in the command prompt
import requests
from bs4 import BeautifulSoup

# prompts the user for to take input of username of the person
username = input("Please enter the username: ")
# gives the instagram url
URL = "https://www.instagram.com/{}/"

# formatting the url by adding username
r = requests.get(URL.format(username))
# using beatifulsoup library parsing
# the html of the website
s = BeautifulSoup(r.text, "html.parser")

# finding the image in the url
# using html parser
u = s.find("meta", property="og:image")
url = u.attrs['content']

# saving the image the folder
# where this file is saved
with open(username + '.jpg', 'wb') as pic:
    binary = requests.get(url).content
    pic.write(binary)
