# Automated Gmail sender

## Key features
- Secure SMTP connection using TLS
- Support for attachments
- Error handling
- Easy to integrate into other Python programs
- Object-oriented design for re-usability

## Setup instructions

To use this script, you'll need to follow these steps:

1. First, set up Google App Password:
- Go to your Google Account settings
- Navigate to Security > 2-Step Verification
- At the bottom, click on "App passwords"
- Generate a new app password for your Python script
- Save this password safely (you'll only see it once)

Note:
In https://myaccount.google.com/security, do you see 2-step verification set to ON? If yes, then visiting https://myaccount.google.com/apppasswords should allow you to set up application specific passwords. 

2. Install "secure-smtplib"
```
pip install secure-smtplib
```

Use the script
```
# Create the sender object
sender = GmailSender("your.email@gmail.com", "your-app-password")

sender.send_email(
    to_email="recipient@example.com",
    subject="Hello!",
    body="This is an automated email."
)

# Use the below script to send the email via attachments
sender.send_email(
    to_email="recipient@example.com",
    subject="Report",
    body="Please find the attached report.",
    attachments=["report.pdf", "data.xlsx"]
)
```

## Author
Mihir Deshpande

## Important security notes:
- Never share your app password
- Don't commit the script with your credentials
- Consider using environment variables for sensitive data