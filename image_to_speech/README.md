USER GUIDE
Setup and activate virtual environment :

For Unix based systems please execute the following command to create venv and install requirements.

make init
source .venv/bin/activate

Pre-requisites

1) Python pillow (PIL)
$ pip install pillow

2) Python pytesseract (py package wrapper)
$ pip install pytesseract

3) Tesseract (OCR Tool)
Download from here https://github.com/tesseract-ocr/tesseract/releases

4) Python pyttsx3 (Text-to-Speech)
$ pip install pyttsx3

How to run the script?

    $ python image_to_speech.py

Once done, Speech would be produced for the given text image