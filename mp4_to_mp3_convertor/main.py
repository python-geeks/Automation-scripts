# MP4 to MP3 Converter

# imported necessary library
from tkinter import Tk, Button, Text, END
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
import moviepy
import moviepy.editor
import os

# created a main window
window = Tk()
window.title('MP4 to MP3 Converter')
window.geometry("1000x700")

# top label
start1 = tk.Label(text="MP4 to MP3 Converter",
                  font=("Arial", 50),
                  fg="magenta")
start1.place(x=130, y=10)

# image on the main window
path = "Images/convert.jpg"
# Creates a Tkinter-compatible photo image
# which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display
# a text or image on the screen.
panel = tk.Label(window, image=img1)
panel.place(x=170, y=120)


def mp4_choose():
    global filename, onlyfilename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Choose MP4",
                                          filetypes=(("Text files", "*.Mp4*"),
                                                     ("all files", "*.*")))
    # Change label contents
    # label_file_explorer.configure(text="File : " + filename)
    onlyfilename = os.path.basename(filename)
    fname.delete('1.0', END)
    fname.insert(END, onlyfilename)


# select label
select1 = tk.Label(text="Select MP4 File : ", font=("Arial", 30), fg="brown")
select1.place(x=50, y=500)

# textarea for file name only
fname = Text(window,
             height=1,
             width=23,
             font=("Arial", 25),
             bg="light yellow",
             fg="brown",
             borderwidth=2,
             relief="solid")
fname.place(x=360, y=505)

# created a choose button , to choose the image from the local system
chooseb = Button(window,
                 text='SELECT',
                 command=mp4_choose,
                 font=("Arial", 17),
                 bg="light green",
                 fg="blue",
                 borderwidth=3,
                 relief="raised")
chooseb.place(x=800, y=500)


# Function for convert Mp4 to Mp3
def convert():
    video = moviepy.editor.VideoFileClip(filename)
    # Convert video to audio
    audio = video.audio

    aud_fname = ""
    for i in onlyfilename:
        if i == '.':
            break
        else:
            aud_fname = aud_fname + i
    print(aud_fname)
    audio.write_audiofile(f'{aud_fname}.mp3')
    mbox.showinfo("Success",
                  "Video converted to Audio.\n\nAudio Saved Successfully")


# created a choose button , to choose the image from the local system
convertb = Button(window,
                  text='CONVERT MP4 To MP3',
                  command=convert, font=("Arial", 20),
                  bg="light green",
                  fg="blue",
                  borderwidth=3,
                  relief="raised")
convertb.place(x=150, y=600)


# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()


# creating an exit button
exitB = Button(window,
               text='EXIT',
               command=exit_win,
               font=("Arial", 20),
               bg="red",
               fg="blue",
               borderwidth=3,
               relief="raised")
exitB.place(x=750, y=600)

# this is done to show the exit dialog box when tried to exit from
# main window using the top-roght close button of titlebar
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
