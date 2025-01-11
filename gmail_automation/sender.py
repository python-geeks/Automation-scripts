import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


class GmailSender:
    def __init__(self, sender_email, app_password):
        self.sender_email = sender_email
        self.app_password = app_password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def create_message(self, to_email, subject, body, attachments=None):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path, "rb") as file:
                        attachment = MIMEApplication(file.read(), _subtype="txt")
                        attachment.add_header(
                            "Content-Disposition",
                            "attachment",
                            filename=os.path.basename(file_path)
                        )
                        message.attach(attachment)

        return message

    def send_email(self, to_email, subject, body, attachments=None):
        """
        Send an email through Gmail.

        Args:
            to_email (str): Recipient's email address
            subject (str): Email subject
            body (str): Email body content
            attachments (list): List of file paths to attach (optional)
        """
        try:
            message = self.create_message(to_email, subject, body, attachments)
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.send_message(message)

            print(f"Email sent successfully to {to_email}")
            return True

        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False


if __name__ == "__main__":
    SENDER_EMAIL = "sender-dude@gmail.com"
    APP_PASSWORD = "<app-password>"  # Generate this from Google Account settings
    gmail_sender = GmailSender(SENDER_EMAIL, APP_PASSWORD)
    gmail_sender.send_email(
        to_email="receiver-dude@example.com",
        subject="Test Email",
        body="Adios!",
        attachments=["path/to/file.txt"]  # Optional
    )
