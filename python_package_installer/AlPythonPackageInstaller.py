import subprocess
from tkinter import*
from tkinter import font
import pyttsx3
from PIL import ImageTk, Image
import os

cwd = os.path.dirname(os.path.realpath(__file__))

class AlPythonPackageInstaller():
    
    def __init__(self):
        root = Tk(className = " ALPYTHONPACKAGEINSTALLER ")
        root.geometry("400x200+1500+815")
        root.resizable(0,0)
        root.iconbitmap(os.path.join(cwd+'\\UI\\icons', 'alpythonpackageinstaller.ico'))
        root.config(bg="#0d4b98")
        root.overrideredirect(1)
        color = '#0d4b98'

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

        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(audio)
            engine.runAndWait()

        def install():
            text.delete(1.0, END)
            package = pythonPackage.get()
            check = subprocess.getoutput('pip install ' + package)
            if '==' in package:
                package = package.split('==')[0]
            alreadyInstalled = 'Requirement already satisfied: ' + package
            nowInstalled = 'Successfully installed ' + package
            errorInstalling = 'ERROR: Could not find a version that satisfies the requirement ' + package
            someError = 'ERROR: '

            if nowInstalled in check.split('\n')[-1]:
                text.insert(1.0, check.split('\n')[-1])
                speak('Successfully installed ' + package)
            elif len(check.split('\n')) >= 3 and nowInstalled in check.split('\n')[-3]:
                text.insert(1.0, check.split('\n')[-3])
                speak('Successfully installed ' + package)
            elif alreadyInstalled in check.split('\n')[0]:
                text.insert(1.0, check.split('\n')[0])
                speak(package + 'already installed')
            elif errorInstalling in check or someError in check:
                text.insert(1.0, check)
                speak('Error installing ' + package)

        textHighlightFont = font.Font(family='OnePlus Sans Display', size=12)
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12, weight='bold')

        #title bar
        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(os.path.join(cwd+'\\UI\\icons', 'alpythonpackageinstaller.ico'))
        icon = icon.resize((30,30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0,column=0,sticky="nsew")
        titleLabel = Label(titleBar, text='ALPYTHONPACKAGEINSTALLER', fg='#909090', bg='#141414', font=appHighlightFont)
        titleLabel.grid(row=0,column=1,sticky="nsew")
        closeButton = Button(titleBar, text="x", bg='#141414', fg="#909090", borderwidth=0, command=root.destroy, font=appHighlightFont)
        closeButton.grid(row=0,column=3,sticky="nsew")
        minimizeButton = Button(titleBar, text="-", bg='#141414', fg="#909090", borderwidth=0, command=hideScreen, font=appHighlightFont)
        minimizeButton.grid(row=0,column=2,sticky="nsew")
        titleBar.grid_columnconfigure(0,weight=1)
        titleBar.grid_columnconfigure(1,weight=75)
        titleBar.grid_columnconfigure(2,weight=1)
        titleBar.grid_columnconfigure(3,weight=1)
        titleBar.pack(fill=X)

        #package widget
        pythonPackage = Label(root, text="PACKAGE NAME")
        pythonPackage.pack()
        pythonPackage.config(bg=color,fg="#fcf2f0",font=textHighlightFont)
        pythonPackage= Entry(root, bg="#ffdf14", fg='#0e3b74', highlightbackground=color, highlightcolor=color, highlightthickness=3, bd=0,font=appHighlightFont)
        pythonPackage.pack(fill=X)

        #install button
        install = Button(root, borderwidth=0, highlightthickness=3, text="INSTALL", command=install)
        install.config(bg=color,fg="#fcf2f0",font=textHighlightFont)
        install.pack(fill=X)

        text = Text(root, font="sans-serif",  relief=SUNKEN , highlightbackground=color, highlightcolor=color, highlightthickness=5, bd=0)
        text.config(bg="#ffdf14", fg='#0e3b74', height=2, font=appHighlightFont)
        text.pack(fill=BOTH, expand=True)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        root.mainloop()

if __name__ == "__main__":
    AlPythonPackageInstaller() 