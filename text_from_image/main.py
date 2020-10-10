import cv2
import sys
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(Image.open(r'D:\\PersonalProjects\\temp\\Text from Image\\test.png'), lang='eng')
file = open(r'D:\\PersonalProjects\\temp\\Text from Image\\output.txt', 'w')
file.write(text)
file.close()