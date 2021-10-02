import tkinter
import sounddevice as sd
import soundfile as sf
from tkinter import *
import sys


def rec10s():
    rec(10)


def rec5s():
    rec(5)


def rec15s():
    rec(15)


def rec(duration):
    fs = 48000

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    return sf.write("assets\\recordings\\AudioNote{}.flac".format(str(sys.argv[1])), recording, fs)


def playback():
    try:
        filename = "assets\\recordings\\AudioNote{}.flac".format(str(sys.argv[1]))
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        sd.wait()
    except:
        pass


master = Tk()
master.title("Audio Note {}".format(str(sys.argv[1])))

Label(master, text=" Record for: (sec) ").grid(row=0, sticky=tkinter.W, rowspan=5, padx=15)

b = Button(master, text="5", command=rec5s)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=10, pady=10)

c = Button(master, text="10", command=rec10s)
c.grid(row=0, column=4, columnspan=2, rowspan=2, padx=10, pady=10)

d = Button(master, text="15", command=rec15s)
d.grid(row=0, column=6, columnspan=2, rowspan=2, padx=10, pady=10)

Label(master, text=" Playback: ").grid(row=5, sticky=W, rowspan=5, padx=15)

e = Button(master, text="Listen to the note", command=playback)
e.grid(row=5, column=3, columnspan=5, padx=10, pady=10)

Label(master, text=" ").grid(row=10, sticky=tkinter.W, rowspan=5)

tkinter.mainloop()
