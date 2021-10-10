import PyPDF2
import heapq
from docx import Document
import re
import os
from tkinter import Tk, END, Frame, SUNKEN, BOTH
from tkinter import font, X, Label, Button, Text, Entry
from PIL import ImageTk, Image
import nltk

nltk.download('punkt')
nltk.download('stopwords')
cwd = os.path.dirname(os.path.realpath(__file__))


class AlDocSummarizer():
    def __init__(self):
        root = Tk(className=" ALDOCSUMMARIZER ")
        root.geometry("550x250+1350+765")
        root.resizable(0, 0)
        root.iconbitmap(os.path.join(cwd + '\\UI\\icons',
                        'aldocsummarizer.ico'))
        root.config(bg="#0098c0")
        root.overrideredirect(1)
        color = '#0098c0'

        def callback(event):
            root.geometry("400x175+1500+840")

        def showScreen(event):
            root.deiconify()
            root.overrideredirect(1)

        def screenAppear(event):
            root.overrideredirect(1)

        def hideScreen():
            root.overrideredirect(0)
            root.iconify()

        def summarize():
            filename = fileText.get()
            filepath = os.path.join(cwd + '\\AlDocSummarizer', filename)
            if os.path.exists(filepath):
                articleText = ''
                extension = os.path.splitext(filepath)[1]
                try:
                    if extension.lower() == ".pdf":
                        pdfFileObj = open(filepath, 'rb')
                        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                        for i in range(pdfReader.numPages):
                            pageObj = pdfReader.getPage(i)
                            articleText += pageObj.extractText()
                        pdfFileObj.close()
                    elif extension.lower() == ".docx":
                        document = Document(filepath)
                        for paragraph in document.paragraphs:
                            articleText += paragraph.text

                    articleText = re.sub(r'\[[0-9]*\]', ' ', articleText)
                    articleText = re.sub(r'\s+', ' ', articleText)
                    formattedArticleText = re.sub('[^a-zA-Z]', ' ',
                                                  articleText)
                    formattedArticleText = re.sub(r'\s+', ' ',
                                                  formattedArticleText)
                    sentenceList = nltk.sent_tokenize(articleText)
                    stopwords = nltk.corpus.stopwords.words('english')
                    wordFreq = {}
                    for word in nltk.word_tokenize(formattedArticleText):
                        if word not in stopwords:
                            if word not in wordFreq.keys():
                                wordFreq[word] = 1
                            else:
                                wordFreq[word] += 1

                    maxFreq = max(wordFreq.values())
                    for word in wordFreq.keys():
                        wordFreq[word] = wordFreq[word] / maxFreq

                    sentenceScores = {}
                    for sent in sentenceList:
                        for word in nltk.word_tokenize(sent.lower()):
                            if word in wordFreq.keys():
                                if len(sent.split(' ')) < 30:
                                    if sent not in sentenceScores.keys():
                                        sentenceScores[sent] = wordFreq[word]
                                    else:
                                        sentenceScores[sent] += wordFreq[word]

                    summarySentences = heapq.nlargest(int(lines.get()),
                                                      sentenceScores,
                                                      key=sentenceScores.get)
                    summaryFileName = filename.replace(extension, '')
                    extension = extension.replace('.', '')
                    summaryFileName = f'{summaryFileName}_{extension}_'
                    summaryFileName += 'summarized.txt'
                    summaryFilePath = os.path.join(cwd + '\\AlDocSummarizer\\'
                                                   'Summarize',
                                                   summaryFileName)
                    summaryFile = open(summaryFilePath, "w")
                    summaryFile.writelines(summarySentences)
                    summaryFile.close()
                    text.delete(1.0, END)
                    text.insert(1.0, summaryFileName + ' has been saved '
                                'successfully in Summarize folder')
                except Exception as e:
                    text.delete(1.0, END)
                    print(str(e))
                    text.insert(1.0, 'Invalid document, please provide .pdf or'
                                ' .docx extension files')
            else:
                text.delete(1.0, END)
                text.insert(1.0, 'Invalid file path')

        textHighlightFont = font.Font(family='OnePlus Sans Display', size=12)
        appHighlightFont = font.Font(family='OnePlus Sans Display', size=12,
                                     weight='bold')

        titleBar = Frame(root, bg='#141414', relief=SUNKEN, bd=0)
        icon = Image.open(os.path.join(cwd + '\\UI\\icons',
                                       'aldocsummarizer.ico'))
        icon = icon.resize((30, 30), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        iconLabel = Label(titleBar, image=icon)
        iconLabel.photo = icon
        iconLabel.config(bg='#141414')
        iconLabel.grid(row=0, column=0, sticky="nsew")
        titleLabel = Label(titleBar, text='ALDOCSUMMARIZER', fg='#909090',
                           bg='#141414', font=appHighlightFont)
        titleLabel.grid(row=0, column=1, sticky="nsew")
        closeButton = Button(titleBar, text="x", bg='#141414', fg="#909090",
                             borderwidth=0, command=root.destroy,
                             font=appHighlightFont)
        closeButton.grid(row=0, column=3, sticky="nsew")
        minimizeButton = Button(titleBar, text="-", bg='#141414', fg="#909090",
                                borderwidth=0, command=hideScreen,
                                font=appHighlightFont)
        minimizeButton.grid(row=0, column=2, sticky="nsew")
        titleBar.grid_columnconfigure(0, weight=1)
        titleBar.grid_columnconfigure(1, weight=30)
        titleBar.grid_columnconfigure(2, weight=1)
        titleBar.grid_columnconfigure(3, weight=1)
        titleBar.pack(fill=X)

        fileText = Label(root, text="DOCUMENT TO BE SUMMARIZED")
        fileText.pack()
        fileText.config(bg=color, fg="white", font=appHighlightFont)
        fileText = Entry(root, bg="white", fg=color, highlightbackground=color,
                         highlightcolor=color, highlightthickness=3, bd=0,
                         font=textHighlightFont)
        fileText.pack(fill=X)

        lines = Label(root, text="NUMBER OF LINES IN WHICH DOCUMENT HAS TO"
                      " SUMMARIZED")
        lines.pack()
        lines.config(bg=color, fg="white", font=appHighlightFont)
        lines = Entry(root, bg="white", fg=color, highlightbackground=color,
                      highlightcolor=color, highlightthickness=3, bd=0,
                      font=textHighlightFont)
        lines.pack(fill=X)

        docSummary = Button(root, borderwidth=0, highlightthickness=3,
                            text="SUMMARIZE", command=summarize)
        docSummary.config(bg=color, fg="white", font=appHighlightFont)
        docSummary.pack(fill=X)

        text = Text(root, font="sans-serif", relief=SUNKEN,
                    highlightbackground=color, highlightcolor=color,
                    highlightthickness=5, bd=0)
        text.config(bg="white", fg=color, height=2, font=textHighlightFont)
        text.pack(fill=BOTH, expand=True)

        titleBar.bind("<B1-Motion>", callback)
        titleBar.bind("<Button-3>", showScreen)
        titleBar.bind("<Map>", screenAppear)

        root.mainloop()


if __name__ == "__main__":
    AlDocSummarizer()
