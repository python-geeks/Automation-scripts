#!/usr/bin/env python3

import smtplib
import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "apeera786@gmail.com"
sender_password = "xxiz ccwg gqtl thhl"
recipient_email = "testswe271@gmail.com"
birthday_message = "Happy Birthday! 🎉🎂 Have a wonderful day!"

def send_email():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  
        server.login(sender_email, sender_password)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "Happy Birthday!"

        msg.attach(MIMEText(birthday_message, 'plain'))

        server.sendmail(sender_email, recipient_email, msg.as_string())

        server.quit()

        print("Birthday message sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    # The birthday date you want to send the message (year, month, day)
    birthday_date = datetime.date(2024, 9, 30)

    while True:
        today = datetime.date.today()
        if today == birthday_date:
            send_email()
            break  
        else:
            time.sleep(60 * 60 * 24)
