from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog
import PIL.Image
import tkinter.font as tkFont

root = Tk()
root.title('QR CODE SCANNER')
root.geometry("600x400")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
      initialdir='/home',
      title="Select file",
      filetypes=(
        ("png files", "*.png"),
        ("all files", "*.*")
                )
    )
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(PIL.Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
    result = decode(PIL.Image.open(root.filename))
    data = result[0].data.decode()
    data = " RESULT : {0}".format(data)
    fontStyle = tkFont.Font(family="Lucida Grande", size=15)
    data_label = Label(root, text=data, font=fontStyle).pack()
my_btn = Button(root, text="Select QR code image", command=open).pack()

root.mainloop()
