from textblob import TextBlob
from tkinter import Tk
from tkinter import filedialog

gui = Tk()
gui.filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select file",
                                          filetypes=(("txt files",
                                                      ".txt"),
                                                     ("all files", ".*")))
f = open(gui.filename, 'r')
s = []
for i in f:
    s.append(i)
f.close()
for i in range(len(s)):
    s[i] = TextBlob(s[i])
    s[i] = s[i].correct()
f = open(gui.filename, 'w')
for i in range(len(s)):
    s[i] = str(s[i])
    f.write(s[i])
f.close()
