from tkinter import font, Button, X
from tkinter import Tk, Frame, SUNKEN, Label
from tkcalendar import Calendar
from datetime import datetime
from PIL import ImageTk, Image
import os
import calendar

cwd = os.path.dirname(os.path.realpath(__file__))


class AlCalendar():
    def __init__(self):
        root = Tk(className=" ALCALENDAR ")
        root.geometry("400x250+1500+765")
        root.resizable(0, 0)
        root.iconbitmap(os.path.join(cwd + '\\UI\\icons', 'alcalendar.ico'))
        root.config(bg="#222222")
        root.overrideredirect(1)
        color = '#222222'

        def callback(event):
            root.geometry("500x750+1410+300")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        textHighlightFont = font.Font(family='OnePlus Sans Display', size=12)
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12,
                                     weight='bold')

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(os.path.join(cwd + '\\UI\\icons', 'alcalendar.ico'))
        icon = icon.resize((30, 30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0, column=0, sticky="nsew")
        titleLabel = Label(titleBar, text='ALCALENDAR', fg='#909090',
                           bg='#141414', font=appHighlightFont)
        titleLabel.grid(row=0, column=1, sticky="nsew")
        closeButton = Button(titleBar, text="x", bg='#141414', fg="#909090",
                             borderwidth=0, command=root.destroy,
                             font=appHighlightFont)
        closeButton.grid(row=0, column=3, sticky="nsew")
        minimizeButton = Button(titleBar, text="-", bg='#141414', fg="#909090",
                                borderwidth=0, command=hideScreen,
                                font=appHighlightFont)
        minimizeButton.grid(row=0, column=2, sticky="nsew")
        titleBar.grid_columnconfigure(0, weight=1)
        titleBar.grid_columnconfigure(1, weight=75)
        titleBar.grid_columnconfigure(2, weight=1)
        titleBar.grid_columnconfigure(3, weight=1)
        titleBar.pack(fill=X)

        now = datetime.now()
        weekday = now.weekday()
        weekdayName = calendar.day_name[weekday]
        today = datetime.strftime(now, '%B %d, %Y')
        fullDate = weekdayName + ', ' + today

        date = Label(root, text=fullDate)
        date.pack()
        date.config(bg=color, fg="white", font=textHighlightFont)

        cal = Calendar(root, selectmode='day', year=now.year, month=now.month,
                       day=now.day)
        cal.pack(fill=X)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        root.mainloop()


if __name__ == "__main__":
    AlCalendar()
