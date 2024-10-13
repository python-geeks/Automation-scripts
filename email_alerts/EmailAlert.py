# Before class definition, ensure there are two blank lines
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailAlert:
    def __init__(self, smtp_server, smtp_port, email_user, email_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, subject, body, recipients):
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = ", ".join(recipients)
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Set up the server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()

            # Login to the email server
            server.login(self.email_user, self.email_password)

            # Send the email
            server.sendmail(self.email_user, recipients, msg.as_string())

            # Log success
            print(f"Email sent successfully to {recipients}")

        except Exception as e:
            # Log failure
            print(f"Failed to send email. Error: {str(e)}")
        finally:
            server.quit()


# After the class definition, ensure two blank lines
if __name__ == "__main__":
    email_alert = EmailAlert('smtp.gmail.com', 587, 'your_email@gmail.com', 'your_password')
    email_alert.send_email('Test Subject', 'This is a test email', ['recipient@example.com'])
