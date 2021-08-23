
import smtplib
import ssl

"""Make sure that the gmail you are using have enabled
   less secure app otherwise email will not be sent"""


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "Enter your Email"
    receiver_email = "Again Enter Same Email"
    password = "Enter PassWord of Email"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
            return True
        except Exception as e:
            print(e)
            print("could not login or send the mail.")
            return False
