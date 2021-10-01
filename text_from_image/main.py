import cv2
import pytesseract


tesseract_path = r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"
image_path = "test.png"
file_path = "output.txt"

pytesseract.pytesseract.tesseract_cmd = tesseract_path

img = cv2.imread(image_path)

# extracting the text by using LSTM
text = pytesseract.image_to_string(img, config="-l eng --oem 1")
text = text.replace("-\n", "").replace("\n", " ")

# writing the text
file = open(file_path, "w")
file.write(text)
file.close()

# adding boxes around the words
boxes = pytesseract.image_to_data(img)
for z, box in enumerate(boxes.splitlines()):
    if z != 0:
        box = box.split()

        # if the data has a word
        if len(box) == 12:

            x, y = int(box[6]), int(box[7])
            h, w = int(box[8]), int(box[9])

            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 0, 255), 1)

cv2.imwrite("OCRed.png", img)
cv2.destroyAllWindows()
