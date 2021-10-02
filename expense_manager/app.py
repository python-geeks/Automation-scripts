import db
import tkinter as tk
from tkinter.ttk import Button, Frame, Entry, Label

LARGE_FONT = ("Verdana", 32)


class ExpenseManager:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

    # display function calls for database update deletion and listing added or deleted#
    def added(self, boxaile):
        myLabel = Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=4, column=0)

    def delete(self, boxaile):
        myLabel = Label(boxaile, text="The value was deleted")
        myLabel.grid(row=4, column=0)

    def display_all(self, database):
        select_all = database
        return select_all

    def insert(self, database, val1, val2, val3):
        goods = val1.get()
        price = val2.get()
        date = val3.get()
        insertion = database(goods, price, date)
        return insertion

    def find_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        find = database(goods, price)
        return find

    def delete_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        delete = database(goods, price)
        return delete

    # MAIN WINDOW
    def main_window(self):
        button1 = Button(self.frame, text="Groceries expenses", command=self.groceries)
        button1.pack()

        button2 = Button(self.frame, text="Household expenses", command=self.household)
        button2.pack()

        button3 = Button(self.frame, text="Entertainment expenses", command=self.entertainment)
        button3.pack()

        button4 = Button(self.frame, text="Other expenses", command=self.other)
        button4.pack()

        button5 = Button(self.frame, text="EXIT", command=exit)
        button5.pack()

    # INSERT VALUES
    def groceries(self):
        top = tk.Toplevel(self.frame)
        top.title('Groceries expenses')
        Label(top, text="Name of good").grid(row=1, column=0, sticky=tk.W, pady=2)
        Label(top, text="Price").grid(row=2, column=0, sticky=tk.W, pady=2)
        Label(top, text="Date of purchase").grid(row=3, column=0, sticky=tk.W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=tk.W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=tk.W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=tk.W, pady=2)

        text = tk.Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS

        B1 = Button(top, text="Insert Values", command=lambda: (self.insert(db.insert_groceries, e1, e2, e3),
                    self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, tk.END),
                    text.insert(tk.END, self.display_all(db.select_all_groceries()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, tk.END),
                    text.insert(tk.END, self.find_expense(db.select_grocery, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense", command=lambda: (self.delete_expense(db.delete_grocery, e1, e2),
                                                                 self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    def household(self):
        top = tk.Toplevel(self.frame)
        top.title('Household expenses')
        Label(top, text="Name of good").grid(row=1, column=0, sticky=tk.W, pady=2)
        Label(top, text="Price").grid(row=2, column=0, sticky=tk.W, pady=2)
        Label(top, text="Date of purchase").grid(row=3, column=0, sticky=tk.W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=tk.W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=tk.W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=tk.W, pady=2)

        text = tk.Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS###

        B1 = Button(top, text="Insert Values",
                    command=lambda: (self.insert(db.insert_household, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, tk.END),
                    text.insert(tk.END, self.display_all(db.select_all_household()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, tk.END),
                    text.insert(tk.END, self.find_expense(db.select_household, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense",
                    command=lambda: (self.delete_expense(db.delete_household, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    def entertainment(self):
        top = tk.Toplevel(self.frame)
        top.title('Entertainment expenses')
        Label(top, text="Name of good").grid(row=1, column=0, sticky=tk.W, pady=2)
        Label(top, text="Price").grid(row=2, column=0, sticky=tk.W, pady=2)
        Label(top, text="Date of purchase").grid(row=3, column=0, sticky=tk.W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=tk.W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=tk.W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=tk.W, pady=2)

        text = tk.Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS

        B1 = Button(top, text="Insert Values",
                    command=lambda: (self.insert(db.insert_entertrainment, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(1.0, tk.END),
                    text.insert(tk.END, self.display_all(db.select_all_entertrainment()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(1.0, tk.END),
                    text.insert(tk.END, self.find_expense(db.select_entertainment, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense",
                    command=lambda: (self.delete_expense(db.delete_entertainment, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)

    def other(self):
        top = tk.Toplevel(self.frame)
        top.title('Entertainment expenses')
        Label(top, text="Name of good").grid(row=1, column=0, sticky=tk.W, pady=2)
        Label(top, text="Price").grid(row=2, column=0, sticky=tk.W, pady=2)
        Label(top, text="Date of purchase").grid(row=3, column=0, sticky=tk.W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=tk.W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=tk.W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=tk.W, pady=2)

        text = tk.Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        # BUTTONS###

        B1 = Button(top, text="Insert Values",
                    command=lambda: (self.insert(db.insert_other, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (
            text.delete(1.0, tk.END), text.insert(tk.END, self.display_all(db.select_all_other()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (
            text.delete(1.0, tk.END), text.insert(tk.END, self.find_expense(db.select_other, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense",
                    command=lambda: (self.delete_expense(db.delete_other, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)


def main():
    # db.create_tables(connection)
    root = tk.Tk()
    root.geometry('600x500')
    root.title("Expense Manager")
    ExpenseManager(root)
    root.mainloop()


main()
