import pytesseract
from PIL import Image
path = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path
image = r'D:\\PersonalProjects\\temp\\Text from Image\\test.png'
text = pytesseract.image_to_string(Image.open(image), lang='eng')
file = open(r'D:\\PersonalProjects\\temp\\Text from Image\\output.txt', 'w')
file.write(text)
file.close()
