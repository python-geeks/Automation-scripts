import os
import sys
from PyPDF2 import PdfFileMerger
from pdf2image import convert_from_path

sys.path.insert(1, '''B:/Production_Programs/Github/
        Automation-scripts/Pdf_to_image/sample_files''')

fileName = "myfile.pdf"
if os.path.exists(fileName):
    os.remove(fileName)

# merge pdfs into one
x = [a for a in os.listdir() if a.endswith(".pdf")]
merger = PdfFileMerger()
for pdf in x:
    merger.append(open(pdf, 'rb'))

with open(fileName, "wb") as fout:
    merger.write(fout)

# convert merged pdf to png files
images = convert_from_path(fileName)

for i, image in enumerate(images):
    fname = 'image' + str(i) + '.png'
    image.save(fname, "PNG")

print("all file converted")
