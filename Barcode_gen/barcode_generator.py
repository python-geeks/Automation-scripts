import barcode
from barcode.writer import ImageWriter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def generate_barcode():
    try:
        ean = ean_entry.get()
        if not ean.isdigit():
            messagebox.showerror("Error", "EAN must be a number.")
            return
        
        # Generate barcode
        my_code = barcode.EAN13(ean, writer=ImageWriter())
        my_code.save("barcode")

        # Display success message
        messagebox.showinfo("Success", "Barcode generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
root = Tk()
root.title("Barcode Generator")

# EAN label and entry
ean_label = Label(root, text="Enter EAN:")
ean_label.grid(row=0, column=0, padx=10, pady=10)
ean_entry = Entry(root)
ean_entry.grid(row=0, column=1, padx=10, pady=10)

# Generate button
generate_button = Button(root, text="Generate Barcode", command=generate_barcode)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()