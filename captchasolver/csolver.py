import pytesseract
import sys
import os
from PIL import Image

# Set Tesseract location
pytesseract.pytesseract.tesseract_cmd = ""

# Image
im = sys.argv[1]


def resize_image(img):
    img = Image.open(img)
    img = img.resize((1000, 500), Image.NEAREST)
    img.save("resized.png")


def solve(img):
    resize_image(img)
    cr = pytesseract.image_to_string("resized.png")
    os.remove("resized.png")
    # First resize captcha and try to read it.
    if cr != "\x0c":
        print(cr)
    else:
        # If it can't read try to read in normal size
        cr = pytesseract.image_to_string(im)
        print(cr)


# Run
solve(im)
