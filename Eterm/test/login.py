import sys
from smtplib import SMTP_SSL, SMTPAuthenticationError
from colorama import Fore

def check(email, password):
    with SMTP_SSL('smtp.gmail.com', 465) as session: # Make a session
        try:
            session.login(email, password) # Login to the server
            print("Logged in")
        except SMTPAuthenticationError:
            sys.exit(f'{Fore.RED}[-] Wrong credentials{Fore.RESET}')

check()