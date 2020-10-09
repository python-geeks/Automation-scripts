import tkinter as tk
from tkinter import RIGHT, TOP, CENTER, X
from tkinter.filedialog import Button, Tk
from tkinter import filedialog
import vlc

# Define root
root = Tk()
root.title("Music Player")

# Set default label text
label_text = tk.StringVar()
label_text.set("")


def pick_music():
    global music_path, label_text
    # Get chosen files path
    music_path = filedialog.askopenfilename(
        filetypes=(("mp3 files", "*.mp3"), ("waw files", "*.waw")))
    # Set music name label text
    label_text.set(music_path.split("/")[-1])
    # Set button states to normal
    stop_music_button["state"] = "normal"
    pause_music_button["state"] = "normal"
    play_music_button["state"] = "normal"


def play_music():
    global p
    # If song playing try to stop
    try:
        p.stop()
    except Exception:
        pass
    p = vlc.MediaPlayer(r"file:///" + music_path)
    # Start music
    p.play()
    # Change play button state to disabled
    play_music_button["state"] = "disabled"


def stop_music():
    p.stop()
    play_music_button["state"] = "normal"


def pause_music():
    p.pause()


# Pick music button
pck_btn = Button(
    root,
    text="Pick Music",
    font="Rockwell",
    relief="flat",
    command=pick_music)
pck_btn.pack(side=TOP)

# Music name label
msc_nme_lbl = tk.Label(
    root,
    justify=CENTER,
    textvariable=label_text)
msc_nme_lbl.pack(side=TOP, fill=X, padx=10)

# Stop music button
stop_music_button = Button(
    root,
    text="Stop",
    font="Rockwell",
    relief="flat",
    command=stop_music)
stop_music_button.pack(side=RIGHT)

# Pause music button
pause_music_button = Button(
    root,
    text="Pause",
    font="Rockwell",
    relief="flat",
    command=pause_music)
pause_music_button.pack(side=RIGHT)

# Play music button
play_music_button = Button(
    root,
    text="Play",
    font="Rockwell",
    relief="flat",
    command=play_music)
play_music_button.pack(side=RIGHT)

# Set default button satates to disabled
stop_music_button["state"] = "disabled"
pause_music_button["state"] = "disabled"
play_music_button["state"] = "disabled"

root.mainloop()
