from PIL import Image
from os.path import getsize
from tkinter.filedialog import askopenfilename, asksaveasfilename


def compress():
    file_path = askopenfilename(title="select image ")
    img = Image.open(file_path)

    print(f"Original size of image was : {getsize(file_path)} Bytes")

    height, width = img.size
    img = img.resize((height, width), Image.ANTIALIAS)

    save_path = asksaveasfilename(title="save compressed image")
    save_path += "_compressed.JPG"
    img.save(save_path)

    print(f"New size of image is       : {getsize(save_path)} Bytes")


if __name__ == '__main__':
    compress()
