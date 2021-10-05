import tkinter as tk
from tkinter import messagebox


def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!')


ws = tk.Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#686e70')
var = tk.IntVar()
frame = tk.Frame(ws, padx=10, pady=10)
frame.pack(expand=True)
age_lb = tk.Label(frame, text="Enter Age (2 - 120)")
age_lb.grid(row=1, column=1)
age_tf = tk.Entry(frame, )
age_tf.grid(row=1, column=2, pady=5)
gen_lb = tk.Label(frame, text='Select Gender')
gen_lb.grid(row=2, column=1)
frame2 = tk.Frame(frame)
frame2.grid(row=2, column=2, pady=5)
male_rb = tk.Radiobutton(frame2, text='Male', variable=var, value=1)
male_rb.pack(side=tk.LEFT)
female_rb = tk.Radiobutton(frame2, text='Female', variable=var, value=2)
female_rb.pack(side=tk.RIGHT)
height_lb = tk.Label(frame, text="Enter Height (cm)  ")
height_lb.grid(row=3, column=1)
weight_lb = tk.Label(frame, text="Enter Weight (kg)  ", )
weight_lb.grid(row=4, column=1)
height_tf = tk.Entry(frame,)
height_tf.grid(row=3, column=2, pady=5)
weight_tf = tk.Entry(frame,)
weight_tf.grid(row=4, column=2, pady=5)
frame3 = tk.Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)
cal_btn = tk.Button(frame3, text='Calculate', command=calculate_bmi)
cal_btn.pack(side=tk.LEFT)
reset_btn = tk.Button(frame3, text='Reset', command=reset_entry)
reset_btn.pack(side=tk.LEFT)
exit_btn = tk.Button(frame3, text='Exit', command=lambda: ws.destroy())
exit_btn.pack(side=tk.RIGHT)
ws.mainloop()
