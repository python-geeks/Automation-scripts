import smtplib
import random
import math
from datetime import date,datetime
now = datetime.now()
time=str(now.strftime("%I:%M %p"))
def mail(email,name):
    content = '\nHello'+name+'\n Thank you using Face recognition based attendance,Your login/logout time has been recorded on'+time+'.\n Thank you' 
    username = "attendance@nmrec.edu.in"
    password = "nmrec@frba"
    sender = "attendance@nmrec.edu.in"
    recipient = email
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo() # identify the computer
    mail.starttls() # transport layer security - encrypt the details
    mail.ehlo()
    mail.login(username,password)
    header = 'To:' + recipient + '\n' + 'From:' + sender + '\n' + 'Subject: PUNCH-IN & PUNCH-OUT \n'
    content = header+content
    #print(content)
    mail.sendmail(sender,recipient,content)
    mail.close
    return(0)
