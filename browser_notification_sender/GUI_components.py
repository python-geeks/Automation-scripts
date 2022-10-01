from tkinter import messagebox, Tk, Label, Text, Button, END
import sender


def run():
    window = Tk()

    window.title("Send Something Cool!")

    window.geometry('420x200')

    lbl = Label(window)

    lbl.grid(column=0, row=0)

    txt = Text(window, width=50, height=5)

    txt.grid(column=2, row=2)

    def clicked():
        message = (txt.get("1.0", END))
        sender.send(message)
        txt.delete("1.0", END)

        messagebox.showinfo("Information",
                            "Your message sent successfully to all linked Devices!")

    btn = Button(window, text="Send", command=clicked, bg="lightgreen", )

    btn.grid(column=2, row=4, ipadx=30, ipady=5, pady=10)

    window.mainloop()
