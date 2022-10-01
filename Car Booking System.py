# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
# DB connection
conn = sqlite3.connect('database.db')

# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []


class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='grey')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=600, height=720, bg='grey')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="Car Booking", font=(
            'georgia 40 bold'), fg='black', bg='grey')
        self.heading.place(x=0, y=0)
        # patients name
        self.name = Label(self.left, text="Owner's Name", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.name.place(x=0, y=100)

        # age
        self.age = Label(self.left, text="Age", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.age.place(x=0, y=140)

        # gender
        self.gender = Label(self.left, text="Gender", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.gender.place(x=0, y=180)

        # location
        self.location = Label(self.left, text="Location", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.location.place(x=0, y=220)

        # appointment time
        self.time = Label(self.left, text="Entry Time", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.time.place(x=0, y=260)

        # phone
        self.phone = Label(self.left, text="Phone Number", font=(
            'georgia 18 bold'), fg='black', bg='grey')
        self.phone.place(x=0, y=300)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        # button to perform a command
        self.submit = Button(self.left, text="Add Booking", width=20,
                             height=2, bg='white', command=self.add_appointment)
        self.submit.place(x=300, y=340)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Booking logs", font=(
            'georgia 28 bold'), fg='black', bg='grey')
        self.logs.place(x=70, y=10)

        self.box = Text(self.right, width=150, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Bookings till now : " +
                        str(self.final_id) + " \n")
    # funtion to call when the submit button is clicked

    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3,
                            self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo(
                "Success", "Booking for " + str(self.val1) + " has been created")
            self.box.insert(END, 'Booking fixed for ' +
                            str(self.val1) + ' at ' + str(self.val5))


# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1366x768")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
