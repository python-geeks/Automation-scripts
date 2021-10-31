import os
from time import sleep
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread

# initialize tkinter GUI
root = tk.Tk()
root.title("YouTube Downloader")

# Global variables to save YT Downloader parameters
ytParams = ""

canvas = tk.Canvas(root, width=650, height=120)
canvas.grid(columnspan=3, rowspan=5)

# YouTube Downloader - title
label = tk.Label(root, text="YouTube Downloader")
label.grid(columnspan=3, row=0, pady=30)
label.configure(font=("Courier", 28, "bold"))

img = Image.open('images/youtube-logo.png')
img = ImageTk.PhotoImage(img)
img_label = tk.Label(image=img)
img_label.image = img
img_label.grid(columnspan=3, row=1)

descTxt = "Download your favorite YouTube videos by entering a URL below."
# Brief tool explanation
desc = tk.Label(root, text=descTxt)
desc.grid(columnspan=3, row=2, pady=10)
desc.configure(font=("Courier", 14))

# Prompts the user to enter a YouTube URL
urlLabel = tk.Label(text="YouTube URL:")
urlLabel.grid(column=0, row=3, pady=20)
urlLabel.configure(font=("Courier", 16))

urlEntry = tk.Entry(root, width=45, borderwidth=2)
urlEntry.grid(column=1, row=3, pady=20)

# Prompts the user to enter a download path if necessary
pathLabel = tk.Label(text="Download Path:")
pathLabel.grid(column=0, row=4, pady=20)
pathLabel.configure(font=("Courier", 16))

pathEntry = tk.Entry(root, width=45, borderwidth=2)
pathEntry.grid(column=1, row=4, pady=20)

downloadButton = tk.StringVar()
downloadButton.set("Download Video")


# Function to alert user that the video is downloading.
class first(Thread):
    def run(self):
        downloadButton.set("Downloading... Please Wait")
        sleep(2)


# Function to run youtube_downloader python script.
class second(Thread):
    def run(self):
        command = "python ../youtube_downloader/ytdownloader.py "
        url = urlEntry.get()
        ytPath = ""

        path = pathEntry.get()
        if path:
            ytPath = " -p " + path

        if not ytPath:
            runPy = command + " " + url
        else:
            runPy = command + " " + url + ytPath
        os.system(runPy)

        downloadButton.set("Download Video")


# Call each function so the class values execute in order.
def downloadVideo():
    first().start()
    second().start()


getVideo = tk.Button(root, textvariable=downloadButton,
                     fg="red", command=downloadVideo,
                     font=("Courier", 15), height=2)
getVideo.grid(columnspan=3, row=6, pady=10)


root.mainloop()
