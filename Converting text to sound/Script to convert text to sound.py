"""
Created on Fri Oct  9 11:40:35 2020

@author: Anustup
"""
## import libraries

from tkinter import tkinter
from gtts import gTTS
from playsound import playsound
root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('DataFlair - TEXT_TO_SPEECH')
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='DataFlair' , font ='arial 15 bold', bg = 'white smoke').pack(side = BOTTOM)
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)
Msg = StringVar()
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)

root.mainloop()
