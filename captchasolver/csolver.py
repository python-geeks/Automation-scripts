import pytesseract, sys, os
from PIL import Image

#Set Tesserat location
pytesseract.pytesseract.tesseract_cmd = "" # Your tesseract location

#Image 
im =  sys.argv[1]

def resize_image(img):
    img = Image.open(img)
    img = img.resize((1000,500),Image.NEAREST)
    img.save("resized.png")

def solve(img):
    #First resize captcha and try to read it 
    resize_image(img)
    cr = pytesseract.image_to_string("resized.png")
    os.remove("resized.png")
    if cr != "\x0c":
        print(cr)
    else:
        #If it cant read try to read in normal size   
        cr = pytesseract.image_to_string(im)
        print(cr)
# Run
solve(im)
