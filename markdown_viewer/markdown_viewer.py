from tkinter import *
from tkinter import font, filedialog, messagebox as mbox
from markdown2 import Markdown
from tkhtmlview import HTMLLabel


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.font = font.Font(family='Helvetica', size=14)
        self.init_window()

    def openfile(self):
        filename = \
            filedialog.askopenfilename(filetypes=(('Markdown File',
                                                   '*.md , *.mdown , *.markdown'),
                                                  ('Text file', '*.txt'),
                                                  ('All files', '*.*')))
        if filename:
            try:
                md2html = Markdown()
                self.outputbox.set_html(md2html.convert(open(filename,
                                                             'r').read()))
            except Exception:
                mbox.showerror('Error opening file',
                               'The selected file cannot be opened !')

    def init_window(self):
        self.master.title('Mardown Viewer')
        self.pack(fill=BOTH, expand=1)

        self.mainmenu = Menu(self)
        self.filemenu = Menu(self.mainmenu)
        self.filemenu.add_command(label='Open', command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.quit)
        self.mainmenu.add_cascade(label='File', menu=self.filemenu)
        self.master.config(menu=self.mainmenu)

        self.outputbox = HTMLLabel(self, width='1', background='white',
                                   html='<h1>Welcome</h1>')
        self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
        self.outputbox.fit_height()


root = Tk()
root.geometry('750x600')
app = Window(root)
app.mainloop()
