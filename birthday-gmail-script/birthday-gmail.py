import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

# Function to send email
def send_birthday_wish(sender_email, app_password, receiver_email, birthday_message):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Happy Birthday! 🎉'
        
        # Add the birthday message to the email
        msg.attach(MIMEText(birthday_message, 'plain'))
        
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, app_password)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        # Disconnect from the server
        server.quit()

        messagebox.showinfo("Success", "Birthday wish sent successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {e}")

# Function to get input from the user and send the email
def send_email():
    sender_email = entry_sender_email.get()
    app_password = entry_app_password.get()
    receiver_email = entry_receiver_email.get()
    birthday_message = text_birthday_message.get("1.0", tk.END)  # Get text from Text widget

    if not sender_email or not app_password or not receiver_email or not birthday_message.strip():
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    send_birthday_wish(sender_email, app_password, receiver_email, birthday_message)

# GUI Setup
app = tk.Tk()
app.title("Birthday Wisher with Gmail")
app.geometry("400x400")

# Gmail sender email label and entry
label_sender_email = tk.Label(app, text="Your Gmail:")
label_sender_email.pack(pady=5)
entry_sender_email = tk.Entry(app, width=40)
entry_sender_email.pack(pady=5)

# App password label and entry
label_app_password = tk.Label(app, text="App Password:")
label_app_password.pack(pady=5)
entry_app_password = tk.Entry(app, show='*', width=40)
entry_app_password.pack(pady=5)

# Recipient email label and entry
label_receiver_email = tk.Label(app, text="Recipient's Email:")
label_receiver_email.pack(pady=5)
entry_receiver_email = tk.Entry(app, width=40)
entry_receiver_email.pack(pady=5)

# Birthday message label and text entry
label_birthday_message = tk.Label(app, text="Birthday Wishes:")
label_birthday_message.pack(pady=5)
text_birthday_message = tk.Text(app, height=5, width=40)
text_birthday_message.pack(pady=5)

# Send button
send_button = tk.Button(app, text="Send Birthday Wish", command=send_email)
send_button.pack(pady=10)

# Run the application
app.mainloop()
