import smtplib
import ssl


def send_email(message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = ""
    receiver_email = ""
    password = ""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print('sent!!!')
            return True
        except Exception as e:
            print(e)
            print("can't send the mail.")
            return False
