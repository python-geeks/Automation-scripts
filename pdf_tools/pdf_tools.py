# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:49:16 2021

@author: gattsu997
"""

# python script to work with pdf docs
# IMPORTANT:: make sure to install PyPDF2 package
# IMPORTANT::keep your pdf file in the SAME file or add path/rename MANUALLY


from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from pathlib import Path

print("this script can print, edit, modify, rotate and add passwords to PDF documents if used properly")
pdf_path = (Path.home() / "myfile.pdf")
pdf = PdfFileReader(str(pdf_path))
print("to get info on your file type INFO")
if input() == "INFO":
    print("documeng title", pdf.documentInfo.title, "\n", "from page 0 to", int
          (pdf.documentInfo.title) - 1)
    print("number of pages:", pdf.getNumPages())
    print("more details:", pdf.documentInfo)
print("to extract pages type OUTPUT")
if input() == "OUTPUT":
    print("do you want the entire text or a specific page? (FULL/PAGE")
    if input() == "FULL":
        for page in pdf.pages:
            print("text will be saved in a txt file")
            with open('fulltext.txt', 'w') as f:
                f.write(page.extractText())
    if input() == "PAGE":
        print("which page do you want?")
        n = int(input())
        page = pdf.getPage(n)
        print(page.extractText())
print("to make a modified pdf type PDF")
if input() == "PDF":
    input_pdf = PdfFileReader(str(pdf_path))
    while input() != "NO":
        print("which page do you want to add to new PDF?")
        pg = input_pdf.getPage(int(input()))
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pg)
        with Path("sliced.pdf").open(mode="wb") as output_file:
            pdf_writer.write(output_file)
        print("add more pages (YES/NO)")
print("if you want to concatenate two PDF docs, type ADD")
if input() == "ADD":
    BASE_PATH = (Path.home())
    print("name the two files eg file1.pdf, file2.pdf one by one")
    m = input()
    n = input()
    pdf_paths = [BASE_PATH / m, BASE_PATH / n]
    pdf_merger = PdfFileMerger()
    for path in pdf_paths:
        pdf_merger.append(str(path))
    output_path = Path.home() / "concatenated.pdf"
    with output_path.open(mode="wb") as output_file:
        pdf_merger.write(output_file)
print("if you want to rotate all pages clockwise write CW or write ACW for anticlockwise")
if input() == "CW":
    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()
    for page in pdf_reader.pages:
        rotated_page = page.rotateClockwise(90)
        pdf_writer.addPage(rotated_page)
if input == "ACW":
    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()
    for page in pdf_reader.pages:
        rotated_page = page.rotateCounterClockwise(90)
        pdf_writer.addPage(rotated_page)
print("if you want to add password to your file type PWD")
if input() == "PWD":
    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()
    pdf_writer.appendPagesFromReader(pdf_reader)
    print("enter password now")
    p = input()
    pdf_writer.encrypt(user_pwd=p)
    output_path = Path.home() / "newsletter_protected.pdf"
    with output_path.open(mode="wb") as output_file:
        pdf_writer.write(output_file)
