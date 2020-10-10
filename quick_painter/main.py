from tkinter import Tk, Button, Canvas
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw

width = 1280
height = 720

background = "#2d2d2d"

image = Image.new("RGB", (width, height), background)
draw = ImageDraw.Draw(image)

window = Tk()
window.title("QuickPaint")
window.geometry(f"{width}x{height}")

color = "#ffffff"


def ButtonColor():
    global color
    colortemp = (colorchooser.askcolor(title="Choose Color"))[1]
    color = colortemp


buttonColor = Button(window, text="Choose Color", command=ButtonColor, width=10)
buttonColor.pack(side="top", fill="y", expand=True, padx=0, pady=0)


def ButtonSave():
    files = [("PNG", "*.png"), ("JPG", "*.jpg")]
    file_ = filedialog.asksaveasfile(filetypes=files, defaultextension=".png")
    print(file_)
    image.save(file_.name)


buttonSave = Button(window, text="Save", command=ButtonSave, width=10)
buttonSave.pack(side="top", fill="y", expand=True, padx=0, pady=0)


def ButtonClear():
    canvas.delete("all")
    draw.rectangle([(0, 0), (width, height)], fill=background)


buttonClear = Button(window, text="Clear", command=ButtonClear, width=10)
buttonClear.pack(side="top", fill="y", expand=True, padx=0, pady=0)
canvas = Canvas(window, bg=background, height=720, width=1000)
canvas.pack()

cursor_ = None


def cursor(event):
    global cursor_
    if cursor_ not in canvas.find_all():
        cursor_ = canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, width=0, fill='cyan')
    canvas.coords(cursor_, event.x - 10, event.y - 10, event.x + 10, event.y + 10)
    canvas.update_idletasks()


def paint(event):
    canvas.coords(cursor_, event.x - 10, event.y - 10, event.x + 10, event.y + 10)

    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    canvas.create_oval(x1, y1, x2, y2, width=0, fill=color)
    draw.ellipse([(event.x - 10, event.y - 10), (event.x + 10, event.y + 10)], fill=color)
    canvas.update_idletasks()


def erase(event):
    canvas.coords(cursor_, event.x - 10, event.y - 10, event.x + 10, event.y + 10)

    item = canvas.find_closest(event.x, event.y)
    coords = canvas.coords(item)
    if (abs(event.x - (coords[0] + 10)) < 35 and abs(event.y - (coords[1] + 10)) < 35):
        canvas.delete(item)
        draw.ellipse([(coords[0], coords[1]), (coords[2], coords[3])], fill=background)


canvas.bind("<B1-Motion>", paint)
canvas.bind("<B3-Motion>", erase)
canvas.bind("<Motion>", cursor)

window.mainloop()
