from tkinter import Tk, Label, Frame, Entry, Button, Listbox, Scrollbar, TclError
from tkinter.font import Font
from tkinter import END, TOP, BOTTOM, ANCHOR, LEFT, BOTH, RIGHT, FLAT
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Error handler in GUI


def err(msg):
    error.config(text=f"Error: {msg}", fg="red", font=('Sans Serif', 18))
    error.pack(pady=20)

# Tkinter button functions


def add_note():
    if len(notes_entry.get()) == 0:
        err("Please enter a note first.")
    else:
        error.pack_forget()
        start_msg.pack_forget()
        notes_list.insert(
            END, f"{notes_list.size() + 1}. " + notes_entry.get())
        notes_entry.delete(0, END)
        notes_list.see("end")


def delete_note():
    try:
        selected = notes_list.get(notes_list.curselection())
        if len(selected) == 0:
            error.config(text="Error: Please select a note first to delete.")
            error.pack()
        else:
            notes_list.delete(ANCHOR)
            if notes_list.size() == 0:
                start_msg.pack(before=notes_list)
        error.pack_forget()
    except TclError:
        err("Select a note to delete")


def check_note():
    try:
        notes_list.itemconfig(
            notes_list.curselection(),
            fg="mediumseagreen",
        )
        notes_list.selection_clear(0, END)
        error.pack_forget()
    except TclError:
        err("Please select a note first.")


def uncheck_note():
    try:
        notes_list.itemconfig(
            notes_list.curselection(),
            fg="black",
        )
        notes_list.selection_clear(0, END)
        error.pack_forget()
    except TclError:
        err("Please select checked note first.")


# Main window
root = Tk()
root.title('Python Sticky notes')
root.geometry('600x600')
root.config(bg='#d3d3d3')
root.iconbitmap("./favicon.ico")
root.resizable(False, False)

# Fonts
my_font = Font(
    family="Sans Serif",
    size=25,
)

# Frame for list items
notes_frame = Frame(root)
notes_frame.pack(pady=10)

# Welcome Message
start_msg = Label(notes_frame, text="Enter a note to get started...", font=(
    "Sans serif", 18), fg="darkgrey")
start_msg.pack(side=TOP)

# Main ListBox for notes
notes_list = Listbox(notes_frame,
                     font=my_font,
                     width=25,
                     height=5,
                     bd=0,
                     bg="SystemButtonFace",
                     selectbackground="grey",
                     activestyle="none",
                     highlightthickness=0
                     )
notes_list.pack(side=LEFT, fill=BOTH)

# Scrollbar for notes_frame
scroll = Scrollbar(notes_frame)
scroll.pack(side=RIGHT, fill=BOTH)

# Scrollbar configuration
notes_list.config(yscrollcommand=scroll.set)
scroll.config(command=notes_list.yview)

# Notes Entry Box
notes_entry = Entry(root, font=("Sans Serif", 22), relief=FLAT, borderwidth=10)
notes_entry.pack(pady=20)

# Button Frame
function_button_frame = Frame(root, bg="#d3d3d3")
function_button_frame.pack()

# Buttons
add_button = Button(function_button_frame, text="Add note", command=add_note)
delete_button = Button(function_button_frame,
                       text="Delete note", command=delete_note)
checked_button = Button(function_button_frame,
                        text="Check item", command=check_note)
unchecked_button = Button(function_button_frame,
                          text="Uncheck item", command=uncheck_note)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=10)
checked_button.grid(row=0, column=2)
unchecked_button.grid(row=0, column=3, padx=10)

# Error Message
error = Label(root)

# Author Info
author = Label(root, text="© Swaraj Baral\nGithub: SwarajBaral",
               bg="#d3d3d3", fg="grey")
author.pack(side=BOTTOM)

if __name__ == '__main__':
    root.mainloop()
