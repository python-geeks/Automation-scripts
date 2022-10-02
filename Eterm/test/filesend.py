# modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# provide information
body = 'Plase find the attachment'
mail_from = 'youremail@gmail.com'
mail_pass = 'sender'
mail_to = ''

message = MIMEMultipart()
message['From'] = mail_from
message['To'] = mail_to
message['Subject'] = 'Email with attachment'

message.attach(MIMEText(body, 'plain'))
files = ['file.pdf']
for file in files:
    with open(file, 'rb') as f:
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((f).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment; filename=%s' % files)
    message.attach(payload)

# setup smtp
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(mail_from, mail_pass)
msg = message.as_string()
session.sendmail(mail_from, mail_to, msg)
session.quit()

# after email message
send_to = mail_to.split('@', 1)
print(f'Email sent to {send_to[0]}')
