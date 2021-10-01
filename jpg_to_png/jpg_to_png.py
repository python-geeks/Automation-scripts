# -*- coding: utf-8 -*-

# import all prerequisites

"""
Created on Tue Aug 31 15:11:50 2021

@author: Ambuj Bharati
"""

import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox

root = tk.Tk()

# title for the output window

root.title('JPG to PNG and ViceVersa')


# function to convert file from jpg to png

def jpg_to_png():
    global im1
    import_filename = fd.askopenfilename()

    if import_filename.endswith('.jpg'):
        im1 = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension='.png')
        im1.save(export_filename)
        messagebox.showinfo('Congratulations ',
                            'Your image is converted to Png ')
    else:
        Label_2 = tk.Label(root, text='Error!', width=20, fg='red',
                           font=('bold', 15))
        Label_2.place(x=80, y=280)
        messagebox.showerror('Fail!!', 'Something Went Wrong.')


# function to convert png file to jpg

def png_to_jpg():
    global im1
    import_filename = fd.askopenfilename()

    if import_filename.endswith('.png'):
        im1 = Image.open(import_filename)
        export_filename = fd.asksaveasfilename(defaultextension='.jpg')
        im1.save(export_filename)
        messagebox.showinfo('Congratulations ',
                            'Your Image is converted to jpg ')
    else:
        Label_2 = tk.Label(root, text='Error!', width=20, fg='red',
                           font=('bold', 15))
        Label_2.place(x=80, y=280)
        messagebox.showerror('Fail!!', 'Something Went Wrong.')


# first button for output window

btn1 = tk.Button(
    root,
    text='Click for JPG to PNG Conversion',
    width=30,
    height=2,
    bg='#22577A',
    fg='white',
    font=('arial', 12, 'bold'),
    command=jpg_to_png)

# coordinates of first button on output window

btn1.place(x=100, y=120)

# second button for output window

btn2 = tk.Button(
    root,
    text='Click for PNG to JPG Coversion',
    width=30,
    height=2,
    bg='#38A3A5',
    fg='white',
    font=('arial', 12, 'bold'),
    command=png_to_jpg)

# coordinates of second button on the output window

btn2.place(x=100, y=220)

# size in pixels of output window which is 500x500

root.geometry('500x500+400+200')
root.mainloop()
