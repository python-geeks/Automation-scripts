from docx import Document
from pdf2docx import parse
import subprocess
import os


def pdf_to_word(pdf_file):

    # convert to dpcx
    word_file = 'word.docx'
    parse(pdf_file, word_file)


def edit_word(find, replacement):

    # open docx file
    word_file = Document('word.docx')
    replace = {find: replacement}

    # scan file and replace text with new text
    for x in replace:
        for line in word_file.paragraphs:
            if line.text.find(x) >= 0:
                line.text = line.text.replace(x, replace[x])

    # exported edited docx
    word_file.save('converted.docx')


def word_to_pdf():

    # export edited docx to pdf
    subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", 'converted.docx'])

    # clean up files
    if os.path.exists("word.docx"):
        os.remove("word.docx")
    if os.path.exists("converted.docx"):
        os.remove("converted.docx")


if __name__ == "__main__":

    # get user input: pdf to edit, text to find, replacement text
    file, find, replacement = input("Your settings (format: file_name.pdf text_to_replace replacement_text): ").split()

    pdf_to_word(file)
    edit_word(find, replacement)
    word_to_pdf()
