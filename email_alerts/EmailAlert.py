import smtplib

def send_email(subject, body, to_email):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, message)
    server.quit()

send_email("Test Alert", "This is an automated email", "recipient@example.com")
