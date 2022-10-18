import os
from pytube import YouTube

home = os.environ["HOME"]
directory = f"{home}/Downloads"
link = input("What is the video link?: ")
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)
print("The video will be placed in your downloads folder.")
yd = yt.streams.get_highest_resolution()
print("Downloading...")
yd.download(directory)
print("Download complete!\nHere is the link to my Github\nif you want to view more of my repositories!\n"
      "https://github.com/Craig-Wildhaber")
