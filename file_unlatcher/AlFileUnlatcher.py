import subprocess
import os
from tkinter import Tk, Label, END, Frame, SUNKEN
from tkinter import font, Button, X, Entry, Text, BOTH
from PIL import ImageTk, Image

cwd = os.path.dirname(os.path.realpath(__file__))


class AlFileUnlatcher():
    def __init__(self):
        root = Tk(className=" ALFILEUNLATCHER ")
        root.geometry("400x175+1500+840")
        root.resizable(0, 0)
        root.iconbitmap(os.path.join(cwd + '\\UI\\icons',
                        'alfileunlatcher.ico'))
        root.config(bg="#ffe69b")
        root.overrideredirect(1)
        color = '#ffe69b'

        def callback(event):
            root.geometry("400x175+1500+840")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        def find():
            inputFile = fileText.get()
            fileName = os.path.join(cwd + '/AlFileUnlatcher',
                                    'files_database.lst')
            if os.path.exists(fileName):
                pass
            else:
                dFile = open(fileName, "x")
                dFile.close()
            filesList = []
            notFoundList = []
            otherList = []
            dFile = open(fileName, "r")
            files = dFile.readlines()
            for file in files:
                file = file.replace('\n', '')
                if os.path.basename(file) == inputFile:
                    if os.path.isfile(file):
                        filesList.append(file)
                    else:
                        notFoundList.append(file)
                else:
                    otherList.append(file)
            dFile.close()
            lines = filesList + otherList
            nFile = open(fileName, "w+")
            for line in lines:
                line += '\n'
                nFile.write(line)
            nFile.close()
            lfl = len(filesList)
            lnfl = len(notFoundList)
            if (lfl == 0) or (lnfl != 0 and lfl == 0) or (lnfl != 0):
                check = subprocess.check_output(f'python {cwd}/AlFileUnlatcher'
                                                '/AlFileSearcher.py "' + ''
                                                '' + inputFile + '"')
                check = check.decode("utf-8").replace('\r\n', ',:;')
                output = check.split(',:;')[:-1]
                allFiles = [i + '\n' for i in output]
                dFile = open(fileName, 'a')
                dFile.writelines(allFiles)
                dFile.close()
                uniqlines = set(open(fileName).readlines())
                bar = open(fileName, 'w+').writelines(set(uniqlines))
                if bar:
                    bar.close()
                for file in output:
                    filename = os.path.basename(file)
                    if filename == inputFile and file not in filesList:
                        filesList.append(file)
            if len(filesList) == 0:
                text.delete(1.0, END)
                text.insert(1.0, 'Invalid input file')
            else:
                for file in filesList:
                    directory = os.path.dirname(file)
                    filename = os.path.basename(file)
                    try:
                        text.delete(1.0, END)
                        text.insert(1.0, 'Opening ' + inputFile)
                        os.startfile(os.path.join(directory, filename))
                    except Exception as e:
                        print(str(e))
                        text.insert(1.0, 'Set a default application to open'
                                    ' the input file')

        textHighlightFont = font.Font(family='OnePlus Sans Display', size=12)
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12,
                                     weight='bold')

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(os.path.join(cwd + '\\UI\\icons',
                          'alfileunlatcher.ico'))
        icon = icon.resize((30, 30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0, column=0, sticky="nsew")
        titleLabel = Label(titleBar, text='ALFILEUNLATCHER', fg='#909090',
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
        titleBar.grid_columnconfigure(1, weight=30)
        titleBar.grid_columnconfigure(2, weight=1)
        titleBar.grid_columnconfigure(3, weight=1)
        titleBar.pack(fill=X)

        fileText = Label(root, text="FILE TO BE SEARCHED AND OPENED")
        fileText.pack()
        fileText.config(bg=color, fg="#0078d7", font=appHighlightFont)
        fileText = Entry(root, bg="#0078d7", fg='white',
                         highlightbackground=color, highlightcolor=color,
                         highlightthickness=3, bd=0, font=textHighlightFont)
        fileText.pack(fill=X)

        find = Button(root, borderwidth=0, highlightthickness=3,
                      text="OPEN FILE", command=find)
        find.config(bg=color, fg="#0078d7", font=appHighlightFont)
        find.pack(fill=X)

        text = Text(root, font="sans-serif", relief=SUNKEN,
                    highlightbackground=color, highlightcolor=color,
                    highlightthickness=5, bd=0)
        text.config(bg="#0078d7", fg='white', height=2, font=textHighlightFont)
        text.pack(fill=BOTH, expand=True)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        root.mainloop()


if __name__ == "__main__":
    AlFileUnlatcher()
