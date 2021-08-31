# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from datetime import datetime
import os
while True:
    now = datetime.now()
    current_time=now.strftime("%H:%M:%S")
    print(current_time)
    if current_time=="11:57:00" or current_time=="11:57:20":
        fromaddr = "attendance@nmrec.edu.in"
        toaddr = "18b61a05c3@nmrec.edu.in"

        # instance of MIMEMultipart 
        msg = MIMEMultipart() 

        # storing the senders email address 
        msg['From'] = fromaddr 

        # storing the receivers email address 
        msg['To'] = toaddr 

        # storing the subject 
        msg['Subject'] = "Subject of the Mail"

        # string to store the body of the mail 
        body = "Body_of_the_mail"

        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 

        # open the file to be sent 
        filename = os.getcwd()+"/images/excel/2021-01-01.xlsx"
        attachment = open(filename, "rb") 

        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 

        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 

        # encode into base64 
        encoders.encode_base64(p) 

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 

        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        s.starttls() 

        # Authentication 
        s.login(fromaddr, "nmrec@frba") 

        # Converts the Multipart msg into a string 
        text = msg.as_string() 

        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 

        # terminating the session 
        s.quit() 
