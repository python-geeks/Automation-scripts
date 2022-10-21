#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Tk
from tkinter import font, filedialog, messagebox as mbox

from click import FileError
from markdown2 import Markdown
from tkhtmlview import HTMLLabel


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.font = font.Font(family="Helvetica", size=14)
        self.init_window()

    def onChange(self, event):
        self.inputeditor.edit_modified(0)
        md2html = Markdown()
        self.outputbox.set_html(md2html.convert(
            self.inputeditor.get("1.0", tk.END)))

    def openfile(self):
        filename = filedialog.askopenfilename(
            filetypes=[
                ("Markdown File", "*.md *.mdown *markdown"),
                ("Text file", "*.txt"),
                ("All files", "*.*"),
            ]
        )
        if filename:
            try:
                self.inputeditor.delete("1.0", tk.END)
                self.inputeditor.insert(tk.END, open(filename, "r").read())
            except FileError:
                mbox.showerror(
                    "Error opening file", "{} \
                     cannot be opened !".format(
                        filename
                    ),
                )

    def savefile(self):
        filedata = self.inputeditor.get("1.0", tk.END)
        filename = filedialog.asksaveasfilename(
            filetypes=(("Markdown file", "*.md"), ("Text file", "*.txt")),
            title="Save Markdown File",
        )
        if filename:
            try:
                f = open(filename, "w")
                f.write(filedata)
            except FileError:
                mbox.showerror("Error saving file", "Unable to save the file")

    def init_window(self):
        self.master.title("Mardown Viewer")
        self.pack(fill=tk.BOTH, expand=1)

        self.mainmenu = tk.Menu(self)
        self.filemenu = tk.Menu(self.mainmenu)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save as", command=self.savefile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.mainmenu.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.mainmenu)

        self.inputeditor = tk.Text(self, width="1", font=self.font)
        self.inputeditor.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.inputeditor.bind("<<Modified>>", self.onChange)

        self.outputbox = HTMLLabel(
            self, width="1", background="white",
            html="<h1>Markdown Editor</h1>"
        )
        self.outputbox.pack(fill=tk.BOTH, expand=1, side=tk.RIGHT)


root = Tk()
root.geometry("750x600")
app = Window(root)
app.mainloop()
