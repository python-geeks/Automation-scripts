import tkinter
import subprocess


def makenew():
    maker(numofwindows)


def maker(wins):
    global numofwindows
    subprocess.Popen(["python.exe", "note.py", str(numofwindows)], shell=True)
    numofwindows = 1 + wins
    maintain()


def maintain():
    global numofwindows
    storage = open("assets\\storage", "w")
    storage.write(str(numofwindows))
    storage.close()


def reset():
    storage = open("assets\\storage", "w")
    storage.write(str(0))
    storage.close()


try:
    getwin = open("assets\\storage", "r")
    win = getwin.readline()
    numofwindows = int(win)
    getwin.close()
    for i in range(0, numofwindows):
        subprocess.Popen(["python.exe", "note.py", str(i)], shell=True)
except FileNotFoundError:
    numofwindows = 0

manager = tkinter.Tk()
manager.title("Audio Notes - Master")

while True:
    try:
        makeNewBtn = tkinter.Button(manager, text='New+', command=makenew)
        makeNewBtn.pack()
        reset = tkinter.Button(manager, text='Reset-', command=reset)
        reset.pack()
        tkinter.mainloop()
    except tkinter.TclError:
        break
