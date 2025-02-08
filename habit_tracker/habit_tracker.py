import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime


# Functions for habit tracking logic
def load_habits():
    try:
        with open('habits.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_habits(habits):
    with open('habits.json', 'w') as file:
        json.dump(habits, file, indent=4)


def add_habit(habit_name):
    habits = load_habits()
    if habit_name not in habits:
        habits[habit_name] = {'streak': 0, 'last_done': None}
    save_habits(habits)


def mark_habit_done(habit_name):
    habits = load_habits()
    today = datetime.now().strftime('%Y-%m-%d')
    if habits.get(habit_name) and habits[habit_name]['last_done'] != today:
        habits[habit_name]['streak'] += 1
        habits[habit_name]['last_done'] = today
        save_habits(habits)
        return True
    return False


def view_habits():
    habits = load_habits()
    return habits


# Tkinter UI Functions
def add_habit_ui():
    habit_name = habit_entry.get()
    if habit_name:
        add_habit(habit_name)
        messagebox.showinfo("Success", f"Habit '{habit_name}"
                                       f"' added successfully!")
    else:
        messagebox.showerror("Error", "Please enter a habit name")


def mark_done_ui():
    habit_name = habit_entry.get()
    if habit_name:
        if mark_habit_done(habit_name):
            messagebox.showinfo("Success", f"Habit '{habit_name}"
                                           f"' marked as done for today!")
        else:
            messagebox.showerror("Error", f"Unable to mark '"f"{habit_name}"
                                          f"' as done. Already done today?")
    else:
        messagebox.showerror("Error", "Please enter a habit name")


def view_habits_ui():
    habits = view_habits()
    habit_list.delete(0, tk.END)
    for habit, info in habits.items():
        habit_list.insert(tk.END, f"{habit}: {info['streak']} "
                                  f"day streak")


# Tkinter UI Setup
root = tk.Tk()
root.title("Habit Tracker")

# Input for habit name
habit_label = tk.Label(root, text="Habit Name:")
habit_label.pack()

habit_entry = tk.Entry(root)
habit_entry.pack()

# Buttons for adding, marking, and viewing habits
add_button = tk.Button(root, text="Add Habit", command=add_habit_ui)
add_button.pack()

done_button = tk.Button(root, text="Mark Habit Done", command=mark_done_ui)
done_button.pack()

view_button = tk.Button(root, text="View Habits", command=view_habits_ui)
view_button.pack()

# Listbox for displaying habits
habit_list = tk.Listbox(root, width=50)
habit_list.pack()

# Run the Tkinter event loop
root.mainloop()
