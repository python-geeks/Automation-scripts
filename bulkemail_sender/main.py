import pandas as pb
import smtplib
import getpass


e = pb.read_excel('list.xlsx')
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
emailid = input("Enter your email id here: ")
server.login(emailid, getpass.getpass(prompt='Password: '))
msg = input("Enter the body message here: ")
subject = input('Enter the subject of the message here: ')
body = 'Subject: {}\n\n{}'.format(subject, msg)
for email in emails:
    server.sendmail(emailid, email, body)
server.quit()
