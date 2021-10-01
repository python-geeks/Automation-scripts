# from re import sub
import tkinter
from tkinter import Tk, Label, StringVar, PhotoImage, HORIZONTAL
# from tkinter.ttk import *
import tkinter.ttk
from tkinter.ttk import Progressbar, Button
from tkinter import filedialog
import time
# from oauthlib.oauth2.rfc6749.clients.base import BODY
import qrcode
# from qrcode.constants import ERROR_CORRECT_H
from googleSourceCode_YT import Create_Service
from googleapiclient.http import MediaFileUpload
import os

# Create variables to store information which are passed to function required to create Google Drive API instance
CLIENT_SECRET_FILE = 'OAuth_Client.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# initialize GUI and set window size
root = Tk()
root.title('QR Code Generator!')
root.geometry("600x400")
root.configure(background="#F6E5FE")

# include all widgets in frame, easy to clear screen
main = tkinter.Frame(root, padx=10, pady=10)
main.pack(padx=10, pady=10)


# Function to clear screen
def clear():
    global main, root
    main.destroy()
    main = tkinter.Frame(root, padx=10, pady=10)
    main.pack(padx=10, pady=10)


# To retrieve text from entry widget, set to instance of StringVar class
entered_text = StringVar()

text_intro = Label(main, text="Convert anything to a QR Code! Select what you want to convert:")
text_intro.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Function to open File explorer to upload file
def openFE():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir='/home',
        title="Select file",
        filetypes=(
            ('PDF files', "*.pdf"),
            ("png files", "*.png"),
            ("all files", "*.*")
        )
    )

    # Uploading file to drive
    head, tail = os.path.split(root.filename)
    file_names = [str(tail)]
    mime_types = ['application/pdf', 'application/vnd.ms-powerpoint', 'image/png', 'image/jpeg', 'application/msword']

    for file_name, mime_type in zip(file_names, mime_types):
        file_metadata = {
            'name': file_name,
        }

        file_path = head + '/{0}'
        media = MediaFileUpload(file_path.format(file_name), mimetype=mime_type)

        extract_filedata = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        file_id = extract_filedata.get('id')
        uploadFiles()

        request_body = {
            'role': 'reader',
            'type': 'anyone'
        }

        service.permissions().create(
            fileId=file_id,
            body=request_body
        ).execute()

        response_share_link = service.files().get(
            fileId=file_id,
            fields='webViewLink'
        ).execute()

    submit(response_share_link['webViewLink'])


my_btn = Button(main, text="Files", command=openFE).grid(row=3, pady=10)


# Retrieving text from entry field to convert to QR code
def submit(anythingElse):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=4
    )

    qr.add_data(anythingElse)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img.save("text_QR.png")
    photo = PhotoImage(file="text_QR.png")
    label = Label(main, image=photo)
    label.photo = photo         # referencing
    label.grid(row=6, column=1, columnspan=2, pady=10)


# Creating Text entry fields
def textbox():
    Label(main, text="Enter your text: ").grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    entryfield = tkinter.Entry(main, textvariable=entered_text, width=50, borderwidth=5, bg="#FEFFE2")
    entryfield.grid(row=4, column=1, pady=20)
    Button(main, text="Submit", command=lambda: [submit(entered_text.get())]).grid(row=5, column=2, columnspan=4)


my_btn2 = Button(main, text="Text", command=lambda: [clear(), textbox()])
my_btn2.grid(row=3, column=1,)


# Progress bar for file upload
def uploadFiles():
    progbar = Progressbar(main, orient=HORIZONTAL, length=200, mode='determinate')
    progbar.grid(row=5, columnspan=3, pady=10)
    for i in range(50):
        if progbar['value'] == 66 or progbar['value'] == 90:
            time.sleep(0.5)
        root.update_idletasks()
        progbar['value'] += 2
        time.sleep(0.02)
    progbar.destroy()
    tkinter.Label(main, text='Upload Successful!', fg='green').grid(row=5, columnspan=3, pady=10)


my_btn3 = Button(main, text="URL", command=lambda: [clear(), textbox()]).grid(row=3, column=2)

root.mainloop()
