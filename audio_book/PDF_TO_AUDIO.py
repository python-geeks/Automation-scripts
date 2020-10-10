import pyttsx3
import PyPDF2
from gtts import gTTS
from tkinter.filedialog import askopenfilename
from tkinter import Tk
Tk().withdraw()
filelocation = askopenfilename()  # open the dialog GUI


book = open(filelocation, 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("No. of pages: ", pages)
speaker = pyttsx3.init()
whole_text = ''
choice = input('choice? ')

if choice == '1':

    for num in range(0, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        whole_text += text
        speaker.say(text)
        print("Reading: ", text)
        speaker.runAndWait()


final_file = gTTS(text=whole_text, lang='en')  # store file in variable
final_file.save("Output Audio.mp3")  # Saving audio file
