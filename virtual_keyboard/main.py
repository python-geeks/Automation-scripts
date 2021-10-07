from tkinter import Tk, Button, END, Label, Canvas, Frame, PhotoImage, NW
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk

root = Tk()
root.title("Virtual Keyboard")
root.geometry('1000x700')


class Keypad(tk.Frame):

    cells = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['!', '@', '#', '$', '%', '&', '*', '/', '\'', '.', ',', ';', ':', '?',
         '<', '>', '😀', '😋', '😂', '🌞', '🌴', '🍕', '🏳', '♻', '✔', '👍'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self,
                              text=item,
                              command=lambda text=item: self.append(text),
                              font=("Arial", 14),
                              bg="light green",
                              fg="blue",
                              borderwidth=3,
                              relief="raised")
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self,
                      text='Space',
                      command=self.space,
                      font=("Arial", 14),
                      bg="light green",
                      fg="blue",
                      borderwidth=3,
                      relief="raised")
        x.grid(row=0, column=10, columnspan='4', sticky='news')

        x = tk.Button(self,
                      text='tab',
                      command=self.tab,
                      font=("Arial", 14),
                      bg="light green",
                      fg="blue",
                      borderwidth=3,
                      relief="raised")
        x.grid(row=0, column=14, columnspan='3', sticky='news')

        x = tk.Button(self,
                      text='Backspace',
                      command=self.backspace,
                      font=("Arial", 14),
                      bg="light green",
                      fg="blue",
                      borderwidth=3,
                      relief="raised")
        x.grid(row=0, column=17, columnspan='3', sticky='news')

        x = tk.Button(self,
                      text='Clear',
                      command=self.clear,
                      font=("Arial", 14),
                      bg="light green",
                      fg="blue",
                      borderwidth=3,
                      relief="raised")
        x.grid(row=0, column=20, columnspan='3', sticky='news')

        x = tk.Button(self,
                      text='Hide',
                      command=self.hide,
                      font=("Arial", 14),
                      bg="light green",
                      fg="blue",
                      borderwidth=3,
                      relief="raised")
        x.grid(row=0, column=23, columnspan='3', sticky='news')

    def get(self):
        if self.target:
            return self.target.get("1.0", "end-1c")

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.target.delete('1.0', 'end')

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def space(self):
        if self.target:
            text = self.get()
            text = text + " "
            self.clear()
            self.append(text)

    def tab(self):  # 5 spaces
        if self.target:
            text = self.get()
            text = text + "     "
            self.clear()
            self.append(text)

    def copy(self):
        # TODO: copy to clipboad
        if self.target:
            self.memory = self.get()
            self.label['text'] = 'memory: ' + self.memory
            print(self.memory)

    def paste(self):
        # TODO: copy from clipboad
        if self.target:
            self.append(self.memory)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.5, anchor='c')

    def hide(self):
        self.target = None

        self.place_forget()

# -------------------------------------------------------


def print_output():
    mbox.showinfo("Text Entered",
                  "Text Entered :\n\n" + text_enter.get('1.0', END))

# firstclick1 = True
# def on_text_enter_click(event):
#     """function that gets called whenever entry1 is clicked"""
#     global firstclick1
#     if firstclick1:  # if this is the first time they clicked it
#         firstclick1 = False
#         text_enter.delete('1.0', "end")  # delete all the text in the entry


def des_f1():
    f1.destroy()


f1 = Frame(root, height=700, width=1000)
f1.propagate(0)
f1.pack(side='top')

# start1 = Label(f1, text='VIRTUAL', font=("Arial", 100), fg="magenta")
# start1.place(x=250, y=100)
#
# start2 = Label(f1, text='KEYBOARD', font=("Arial", 100), fg="magenta")
# start2.place(x=150, y=300)

c = Canvas(f1, width=1000, height=700)
c.pack()
p1 = PhotoImage(file="Images/keyboard.png")
c.create_image(200, 100, image=p1, anchor=NW)

start1 = Label(f1,
               text='VIRTUAL KEYBOARD',
               font=("Arial", 50),
               fg="magenta",
               underline=0)
start1.place(x=150, y=10)

startb = Button(f1,
                text="START",
                command=des_f1,
                font=("Arial", 30),
                bg="light green",
                fg="blue",
                borderwidth=3,
                relief="raised")
startb.place(x=180, y=550)


f2 = Frame(root, height=700, width=1000)
f2.propagate(0)
f2.pack(side='top')

keypad = Keypad(root)

start2 = Label(f2, text='ENTER TEXT HERE...', font=("Arial", 40), fg="magenta")
start2.place(x=200, y=460)

text_enter = tk.Text(f2,
                     height=10,
                     width=80,
                     font=("Arial", 15),
                     bg="light yellow",
                     fg="brown",
                     borderwidth=3,
                     relief="solid")
text_enter.insert(END, 'Enter your text here from virtual keyboard...')
# default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
text_enter.place(x=50, y=10)

keyboardb = Button(f2,
                   text="KEYBOARD",
                   command=lambda: keypad.show(text_enter),
                   font=("Arial", 30),
                   bg="light green",
                   fg="blue",
                   borderwidth=3,
                   relief="raised")
keyboardb.place(x=100, y=550)

printb = Button(f2,
                text="PRINT",
                command=print_output,
                font=("Arial", 30),
                bg="light green",
                fg="blue",
                borderwidth=3,
                relief="raised")
printb.place(x=450, y=550)


def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()


exitb = Button(root,
               text="EXIT",
               command=exit_win,
               font=("Arial", 30),
               bg="red",
               fg="blue",
               borderwidth=3,
               relief="raised")
exitb.place(x=700, y=550)


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
