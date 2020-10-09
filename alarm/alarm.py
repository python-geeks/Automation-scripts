import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time, winsound


def widget():
    label1 = Label(intial, text = 'Enter time h:m')
    label1.grid(row=0, column=0, padx=8, pady=8)


    global entry1
    entry1 = Entry(intial, width = 18)
    entry1.grid(row=0, column=1)

    label2 = Label(intial, text = 'Note')
    label2.grid(row=1, column=0, padx=8, pady=8)


    global entry2
    entry2 = Entry(intial, width = 18)
    entry2.grid(row=1, column=1)

    button = Button(intial, text='Set', width=10,command=submit)
    button.grid(row=2, column=1)

    global label3
    label3  = Label(intial, text='')
    label3.grid(row=3, column=0)

def message():
    global entry1, label3
    Alarmtimelabel = entry1.get()
    label3.config(text='The alarm has been set') 
    messagebox.showinfo('Alarm clock', f'The Alram time is: {Alarmtimelabel}')

def submit():
    global entry1, entry2, label3
    Alarmtime = entry1.get()
    message()
    currenttime = time.strftime('%H:%M')
    print(f"The Alarm time is: {Alarmtime}")
    alarmmessage = entry2.get()
    while Alarmtime != currenttime:
        currenttime = time.strftime('%H:%M')
        time.sleep(1)
    if Alarmtime == currenttime:
        print('Playing Alram')
        winsound.PlaySound('./sound1.wav', winsound.SND_ASYNC)
        label3.config(text='Alarm is Playing') 
        messagebox.showinfo('Alarm Meassgae', f'The Message is: {alarmmessage}')   

intial = tk.Tk()
intial.title("Alarm")
intial.geometry("500x150")

widget()

intial.mainloop()