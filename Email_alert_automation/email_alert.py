import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class EmailAlert:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject, body, recipients):
        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ", ".join(recipients)
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Set up the server connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f'Email sent to {", ".join(recipients)}')

        except Exception as e:
            logging.error(f'Failed to send email: {e}')

if __name__ == "__main__":
    # Example configuration (replace with your actual SMTP server settings)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_email_password'

    # Create an instance of EmailAlert
    email_alert = EmailAlert(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the email content
    subject = 'Critical Event Notification'
    body = 'This is a notification about a critical event that requires your attention.'
    recipients = ['recipient1@example.com', 'recipient2@example.com']

    # Send the email alert
    email_alert.send_email(subject, body, recipients)
