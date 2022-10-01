import pytesseract
from PIL import Image
import pyttsx3
img = Image.open('Location_to_Image/text_image.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_string(img)
with open('text.txt', mode='w') as file:
    file.write(result)
    print(result)
engine = pyttsx3.init()
engine.say(result)
engine.runAndWait()
