# quick sort visualizer

# import tkinter as tk
from tkinter import Tk, Label, Button, Frame, Canvas, Entry, SW, W
from tkinter import messagebox
import random
import time
import sys

sys.setrecursionlimit(10**6)

# colours
DARK_GREY = '#73C6B6'
LIGHT_GREY = '#B2BABB'
WHITE = '#F0F3F4'
GREEN = '#82E0AA'
GREEN_2 = '#76D7C4'
BLUE = '#85C1E9'
PURPLE = '#BB8FCE'
RED = '#F5B7B1'
YELLOW = '#F7E806'

# array of elements / rectangle heights
array = []


# ~30 elements fit in the canvas using below function
def drawRect(array, color):
    canvas.delete("all")
    c_height = 380
    c_width = 1000
    x_width = c_width / (len(array) + 1)
    x_left = 15
    spacing = 10
    normalizedArray = [i / max(array) for i in array]
    for i, height in enumerate(normalizedArray):
        # top left
        x0 = i * x_width + x_left + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + x_left
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(array[i]))

    root.update_idletasks()


# generate random elements for the array and
# draw their rectangles on the canvas
def Generate():
    global array
    try:
        minVal = int(minEntry.get())
        maxVal = int(maxEntry.get())
        size = int(sizeEntry.get())
    except Exception:
        messagebox.showwarning("Message", "Enter all values correctly")

    array = []
    # generating random list
    color = []
    for _ in range(size):
        array.append(random.randrange(minVal, maxVal + 1))
        color.append(GREEN_2)

    drawRect(array, color)


# partition function
def partition(array, left, right, drawRect):
    i = left + 1
    pivot = array[left]

    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1


# quick sort function
def quickSort(array, left, right, drawRect):
    if left < right:
        pivot = partition(array, left, right, drawRect)
        quickSort(array, left, pivot, drawRect)
        quickSort(array, pivot + 1, right, drawRect)
        drawRect(array, [BLUE if x >= left and x < pivot
                         else YELLOW if x == pivot
                         else PURPLE if x > pivot and x <= right
                         else RED for x in range(len(array))])

        time.sleep(0.5)
    drawRect(array, [GREEN for x in range(len(array))])


# actually perform quicksort
def sort():
    try:
        quickSort(array, 0, len(array) - 1, drawRect)
        messagebox.showinfo('Succces', 'Array sorted!')
    except Exception:
        messagebox.showinfo('Error', 'Array could not be sorted')


def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()


# !--GUI code starts--!

# main window
root = Tk()
root.title('Quick Sort Visualizer')
# background color
root.config(bg=LIGHT_GREY)
# disabling resizing of window
root.resizable(0, 0)

# ---adding frames---
# top name frame
top = Frame(root,
            width=1300,
            height=200,
            bg=GREEN_2,
            bd=8,
            relief="groove")
top.grid(row=0, column=0, padx=10, pady=5)

# frame for canvas
canvas = Canvas(root,
                width=1000,
                height=380,
                bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

# frame for user entries
entries = Frame(root,
                width=1300,
                height=300,
                bg=GREEN_2,
                bd=8,
                relief="groove")
entries.grid(row=2, column=0, padx=10, pady=5)


# ---adding widgets---
# top label
greeting = Label(top,
                 text="Quick Sort Visualizer",
                 width=62,
                 font=("Courier New", 20, "bold"),
                 background=GREEN_2)
greeting.grid(row=0, column=1, pady=5)


# user entries and buttons
# row 0
Size = Label(entries,
             text="Size of array : ",
             bg=LIGHT_GREY,
             relief="groove")
Size.grid(row=0,
          column=0,
          padx=15,
          pady=5,
          sticky=W,
          ipadx=20,
          ipady=5)
sizeEntry = Entry(entries, justify="center")
sizeEntry.grid(row=0, column=1, padx=15, pady=5, sticky=W, ipady=5)

minn = Label(entries,
             text="Minimum element : ",
             bg=LIGHT_GREY,
             relief="groove")
minn.grid(row=0, column=2, padx=15, pady=5, sticky=W, ipadx=20, ipady=5)
minEntry = Entry(entries, justify="center")
minEntry.grid(row=0, column=3, padx=15, pady=5, sticky=W, ipady=5)

maxx = Label(entries,
             text="Maximum element : ",
             bg=LIGHT_GREY,
             relief="groove")
maxx.grid(row=0, column=4, padx=15, pady=5, sticky=W, ipadx=20, ipady=5)
maxEntry = Entry(entries, justify="center")
maxEntry.grid(row=0, column=5, padx=15, pady=5, sticky=W, ipady=5)

# row 1
generate = Button(entries, text="Generate", bg=LIGHT_GREY, command=Generate)
generate.grid(row=1, column=2, padx=15, pady=5, ipadx=20, ipady=5)

Search = Button(entries, text="Sort", bg=LIGHT_GREY, command=sort)
Search.grid(row=1, column=3, padx=15, pady=5, ipadx=20, ipady=5)

Exitbtn = Button(entries, text="Exit", bg=LIGHT_GREY, command=exit_win)
Exitbtn.grid(row=1, column=4, padx=15, pady=5, ipadx=20, ipady=5)

root.mainloop()

# !--GUI code ends--!
