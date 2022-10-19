import ctypes
import time
from tkinter import Button, Entry, Frame, Label, Tk
from tkinter.constants import BOTTOM, FLAT, LEFT
from tkinter.font import BOLD
import threading
import os

try:
    import winsound
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass

root = Tk()
root.config(bg="Salmon")
root.geometry('600x500')
root.title("Pomodoro Timer")
root.resizable(0, 0)

POMO_OPTIONS = {
    0: (25, 5),
    1: (20, 10),
}


def user_start():
    custom_work = int(user_input_work.get())
    custom_break = int(user_input_break.get())
    start_timer_params = (custom_work, custom_break)
    return threading.Thread(
        target=start_timer, args=[start_timer_params]).start()


def today():
    day = time.strftime("%a")
    hour = time.strftime("%I")
    minutes = time.strftime("%M")
    ampm = time.strftime("%p")
    date_label.config(text=f"{day} {hour}:{minutes} {ampm}")
    date_label.after(1000, today)


def reset():
    title_label.config(text="Focus...")
    timer_label.config(text="Timer Here")
    root.geometry("600x500")
    button_frame.pack(pady=10)
    cycle_label.pack_forget()
    input_frame.pack(pady=20)
    instruction_label.pack()
    return


def start_timer(options, cycle_limit=5):
    root.geometry("600x250")
    cycles = 1
    _work = int(options[0] * 60)
    _break = int(options[1] * 60)
    button_frame.pack_forget()
    input_frame.pack_forget()
    instruction_label.pack_forget()
    while cycles < cycle_limit:
        cycle_label.config(text=f"Cycle no - {cycles}")
        cycle_label.pack()
        temp_work = _work
        temp_break = _break
        while temp_work:
            title_label.config(text="You should be working now.")
            minutes, seconds = divmod(temp_work, 60)
            timer_label.config(text=f"{minutes}:{seconds}")
            root.update_idletasks()
            time.sleep(1)
            temp_work -= 1
        try:
            winsound.Beep(323, 250)
            winsound.Beep(583, 250)
        except Exception:
            os.system('tput bel')

        while temp_break:
            title_label.config(text="You should be taking a break now.")
            minutes, seconds = divmod(temp_break, 60)
            timer_label.config(text=f"{minutes}:{seconds}")
            root.update_idletasks()
            time.sleep(1)
            temp_break -= 1
        try:
            winsound.Beep(523, 250)
            winsound.Beep(783, 250)
        except Exception:
            os.system('tput bel')
        cycles += 1

    reset()
    return


# Title
title_label = Label(root, text="Focus...",
                    font=("MV Boli", 20, BOLD),
                    bg="Salmon")
title_label.pack()

# Cycle Number
cycle_label = Label(root, font=("Consolas", 20, BOLD),
                    bg="Salmon")

# Pomodoro Timer
timer_label = Label(root, text="Timer here",
                    bg="black", fg="green", font=("Consolas", 32),
                    width=10)
timer_label.pack(pady=20)

# Pomodoro Cycle Button Options
button_frame = Frame(root, bg="salmon")
button_frame.pack(pady=10)

pom_one = Button(button_frame, text="25/5 Cycle", font="Helvetica 12",
                 height=1, width=12,
                 command=lambda: threading.Thread(
                     target=start_timer, args=[POMO_OPTIONS[0]]
                 ).start()
                 )
pom_one.grid(row=0, column=0, padx=5)
pom_two = Button(button_frame, text="20/10 Cycle", font="Helvetica 12",
                 height=1, width=12,
                 command=lambda: threading.Thread(
                     target=start_timer, args=[POMO_OPTIONS[1]]
                 ).start()
                 )
pom_two.grid(row=0, column=1)

# User input time options
input_frame = Frame(root, bg="salmon")
input_frame.pack(pady=20)

custom_label = Label(
    input_frame, text="Enter Custom work/break", bg="salmon", font="Serif 10")
custom_label.grid(row=0, column=0, columnspan=2)

input_label_work = Label(input_frame, text="Work (in mins)",
                         bg="salmon", font="Serif 10")
input_label_break = Label(input_frame, text="Break (in mins)",
                          bg="salmon", font="Serif 10")

input_label_work.grid(row=2, column=0)
input_label_break.grid(row=2, column=1)

user_input_work = Entry(input_frame, font=(
    "Sans Serif", 12), relief=FLAT, width=10)
user_input_break = Entry(input_frame, font=(
    "Sans Serif", 12), relief=FLAT, width=10)

user_input_work.grid(row=1, column=0)
user_input_break.grid(row=1, column=1, padx=10)

user_input_start = Button(input_frame, text="Start",
                          font=("Sans Serif", 8),
                          relief=FLAT, command=user_start)
user_input_start.grid(row=1, column=2)

# Date time label
date_label = Label(root, text="Datetime:",
                   font=("Consolas", 14), bg="salmon")
date_label.pack(side=BOTTOM)


# Instruction Label
instruction_label = Label(
    root,
    text='''
    • Select the predefined pomodoro options
    • Or enter your own work/break timings
    • Work until the work timer ends
    • Take a break until break timer ends
    • This will go on for 4 cycles in total
    ''',
    font="Serif 12 bold",
    justify=LEFT,
    bg="salmon"
)
instruction_label.pack()

if __name__ == "__main__":
    threading.Thread(target=today).start()
    root.mainloop()
