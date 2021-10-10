from tkinter import Tk, Frame, SUNKEN, Label
from tkinter import ttk, Button, X, Text, WORD
from tkinter import font, END
from googletrans import Translator, LANGUAGES
from PIL import ImageTk, Image
import os

cwd = os.path.dirname(os.path.realpath(__file__))


class AlTranslator():

    def __init__(self):
        root = Tk(className=" ALTRANSLATOR ")
        root.geometry("1080x400+820+615")
        root.resizable(0, 0)
        root.iconbitmap(os.path.join(cwd + '\\UI\\icons', 'altranslator.ico'))
        root.config(bg='#ffffff')
        root.overrideredirect(1)

        def callback(event):
            root.geometry("400x130+1510+885")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12,
                                     weight='bold')

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(os.path.join(cwd + '\\UI\\icons',
                          'altranslator.ico'))
        icon = icon.resize((30, 30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0, column=0, sticky="nsew")
        titleLabel = Label(titleBar, text='ALTRANSLATOR', fg='#909090',
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
        titleBar.grid_columnconfigure(1, weight=20)
        titleBar.grid_columnconfigure(2, weight=1)
        titleBar.grid_columnconfigure(3, weight=1)
        titleBar.pack(fill=X)

        inputText = Text(root, font=appHighlightFont, height=11,
                         wrap=WORD, padx=5, pady=5, width=40, fg='#4877bc')
        inputText.place(x=20, y=100)
        outputText = Text(root, font=appHighlightFont, height=11, wrap=WORD,
                          padx=5, pady=5, width=40, bg='#f8f9fb', fg='#4877bc')
        outputText.place(x=610, y=100)

        language = list(LANGUAGES.values())
        srcLang = ttk.Combobox(root, values=language, width=22,
                               font=appHighlightFont)
        srcLang.place(x=20, y=60)
        srcLang.set('Source language')
        destLang = ttk.Combobox(root, values=language, width=22,
                                font=appHighlightFont)
        destLang.place(x=800, y=60)
        destLang.set('Destination language')

        def gTranslate():
            translator = Translator()
            translated = translator.translate(text=inputText.get(1.0, END),
                                              src=srcLang.get().capitalize(),
                                              dest=destLang.get().capitalize())
            outputText.delete(1.0, END)
            outputText.insert(END, translated.text)

        trans_btn = Button(root, text='Translate', font=appHighlightFont,
                           pady=5, command=gTranslate, fg='#8e8d91', width=9,
                           bg='#ffffff', bd=0)
        trans_btn.place(x=500, y=180)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        root.mainloop()


if __name__ == "__main__":
    AlTranslator()
