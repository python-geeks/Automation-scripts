import os
from pytube import YouTube
import moviepy.editor as mp

SAVE_PATH = r"C:\Users\Downloads"
link = input("Paste the link")
video = YouTube(link)
stream = video.streams.filter(only_audio=True).all()
for i in stream:
    print(i)
k = int(input("Type the itag no. you want to download"))
video.streams.get_by_itag(k).download(SAVE_PATH)
m = video.title
print(m + "is downloaded in .mp4 audio format")

text_files = [f for f in os.listdir(SAVE_PATH) if f.endswith('.mp4')]
print(text_files)
s = input("Kindly paste the title you want in .mp3 from above list")

mp4_file = SAVE_PATH + "\\" + s
mp3_file = r"C:\Users\Downloads\newaudio.mp3"


clip = mp.AudioFileClip(mp4_file)
clip.write_audiofile(mp3_file)
os.remove(mp4_file)
print("Done!")
