import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from gtts import gTTS
Tk().withdraw()
filelocation = askopenfilename()  # To select pdf files


pdf_file = open(filelocation, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf_file)
speak = pyttsx3.init()
pages = pdfReader.numPages
complete_pdf = ""
choice = input("Press 1 to dictate or anything else to skip dictation ")
for i in range(0, pages):
    from_page = pdfReader.getPage(i)
    text = from_page.extractText()
    if choice == "1":
        speak.say("Page Number:" + str(i + 1))
        speak.say(text)
    complete_pdf += text
speak.runAndWait()
final_file = gTTS(text=complete_pdf, lang='en')  # store file in variable
file_name = input("Name of the MP3 file: ")
final_file.save(file_name + ".mp3")  # Saving audio file
print("Conversion is Complete")
