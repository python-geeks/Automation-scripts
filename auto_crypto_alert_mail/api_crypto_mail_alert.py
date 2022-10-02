# To install the unsed libraries run the below commands in the terminal
# pip install secure-smtplib
# pip install requests

import requests
import smtplib

'''
<===== IMPORTANT =====>
1. THIS WILL NOT WORK WHEN SENDING MAIL FROM GMAIL BECAUSE OF NEW GOOGLE SECURITY POLICIES.
2. BUT YOU CAN SEND MAIL FROM OUTLOOK OR ANY OTHER MAIL SERVICES WITHOUT ANY PROBLEM.
3. ONLY UPDATE 'from_email', 'from_email_password' & 'to_email'.
4. IF USING ANY OTHER MAIL SERVICE THEN CHANGE THE SERVER AND PORT TOO IN LINE 19 & 20.
'''

# Add your Email ID & it's Password by which you are sending the email alert
from_email = "<SENDER'S_EMAIL_ID>"
from_email_password = "<SENDER'S_EMAIL_PASSWORD>"
mail_port = 587
mail_server = "smtp-mail.outlook.com"

# Add Email ID to whom you want to send the alert
to_email = "RECEIVER'S_EMAIL_ID"


def check_price():
    spot_name = input("Input the crypto currency to get alerts (eg. BTCUSDT): ")
    print("1.If Price hits Above\n2.If Price hits Below\n")
    cpolarity = int(input("Choose from 1 & 2: "))
    trig_point = 1
    if cpolarity == 1:
        trig_point = float(input("Input the trigger price(dollar) above at which you want to recieve mail alert: "))
    else:
        trig_point = float(input("Input the trigger price(dollar) below at which you want to recieve mail alert: "))

    def send_mail():
        server = smtplib.SMTP(mail_server, mail_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(from_email, from_email_password)
        subject = f"{spot_name.upper()} EXCHANGE RATE"

        if cpolarity == 1:
            body = f"{spot_name.upper()} Exchange is now above ${trig_point}: Current Exchange Rate: ${lprice}."
        else:
            body = f"{spot_name.upper()} Exchange is now below ${trig_point}: Current Exchange Rate: ${lprice}."

        msg = f'''Subject: {subject}\n
        To: {"".join(to_email)}\n
        {body}'''

        server.sendmail(from_email, to_email, msg.encode("utf8"))

        print("Alert! The E-mail has been sent!")
        server.quit()

    while True:
        Url = "https://api.binance.com/api/v3/ticker/24hr"
        r = requests.get(Url)
        json_list = r.json()
        cryptoname = {}
        lprice = 0
        for i in range(len(json_list)):
            if json_list[i]["symbol"] == spot_name.upper():
                cryptoname = json_list[i]
        try:
            lprice = float(cryptoname["lastPrice"][4:6])
            print(lprice)
        except ValueError:
            print("This Exchange is not available.")

        if lprice >= trig_point and cpolarity == 1:
            send_mail()
            exit()
        if lprice <= trig_point and cpolarity == 2:
            send_mail()
            exit()


check_price()
