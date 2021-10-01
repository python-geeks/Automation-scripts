import os
from fpdf import FPDF


def converter():
    img_files = os.listdir('images/')
    print('files to be converted: ', img_files)
    pdf = FPDF()
    for image in img_files:
        pdf.add_page()
        pdf.image('images/' + image)
    pdf.output('converted.pdf', 'F')


if __name__ == '__main__':
    converter()
