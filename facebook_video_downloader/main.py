import os
import re
import requests
import urllib

#Getting the link from user
link = input('Enter the video url: ')
name = input('Enter the name of the video: ')

#Getting the HTML data

html = requests.get(link)

#Parsing the data
try:
    url = re.search('hd_src:"(.+?)"', html.text) #hd video
    print('Found video in HD format.')
except:
    url = re.search('sd_src:"(.+?)"', html.text) #sd video
    print('Found video in SD format.')

# #download the file
print('Downloading.......')

if name:
    urllib.request.urlretrieve(url[1], f"{os.path.join('downloaded_videos', name)}.mp4")
else:
    urllib.request.urlretrieve(url[1], f"{os.path.join('downloaded_videos', link[-6:])}.mp4")
print('Video Downloaded Successfully')