#!/usr/bin/python3

import argparse
import getpass
import hashlib
import json
import os
import readline
import smtplib
import socket
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email
from colorama import Fore, init

# File imports
import AutoCompleter
import credsChecker


class EmailSender:
    def __init__(self):
        init(autoreset=True)
        self.parser = argparse.ArgumentParser(description="Send Emails"
                                              " through your terminal.",
                                              epilog="For more info check "
                                                     "my github page "
                                                     "https://github.com/"
                                                     "mrHola21/Eterm/")

        self.get_arguments()

        self.from_email = ""
        self.to_email = ""
        self.body_content_list = []
        self.body_content = ""
        self.files = []
        self.password = b""
        self.server = "smtp.gmail.com"
        self.imap_server = "imap.gmail.com"
        self.port = 587
        self.search = "ALL"

        self.args = self.parser.parse_args()

        self.msg = MIMEMultipart()

        self.check_credentials()

    def get_arguments(self):
        self.parser.add_argument('from_', metavar="sender's email address", )
        self.parser.add_argument('--to', '-t', metavar="Receivers"
                                 " email", help="receiver's "
                                 "email address")
        self.parser.add_argument('--subject', '-s', action="store_tr"
                                 "ue", help="Add Subject to your Email.")
        self.parser.add_argument('--body', '-b', action="store_"
                                 "true", help="Add the body to your Email")
        self.parser.add_argument('--file', '-f', metavar="File", type=str,
                                 nargs='+', help="Add Files to"
                                 " your emails")
        self.parser.add_argument('--listall', '-L', action="store_"
                                 "true", help='show all emails')
        self.parser.add_argument('--list', '-l', metavar="number of"
                                 " emails to show", action="store", type=int)
        self.parser.add_argument('--verbose', '-v', action="store"
                                 "_true", help="Get Expanded Emails")
        self.parser.add_argument('--search', help="Search for"
                                 " a specific email")
        self.parser.add_argument('--server', '-S', metavar="server"
                                 " name", type=str, help="Change "
                                 "The SMTP server.Default is 'smtp.gmail.com'")
        self.parser.add_argument('--imapserver', '-i', metavar="imap"
                                 " server", type=str, help="Change"
                                 " The Imap Server.Default"
                                 " is 'imap.gmail.com'")
        self.parser.add_argument('--port', '-p', metavar="port"
                                 " number", type=int, help="Change The"
                                 " SMTP server's port.Default is 587")

    def route(self):
        if self.args.list is not None or self.args.listall or self.args.search:
            self.read_email()
        else:
            self.send_email_file()

    def new_email(self):
        password = bytes(
            getpass.getpass(
                'First Time Entering '
                'The Password For '
                f'{Fore.BLUE}{self.args.from_} {Fore.RESET}:'), 'utf8')
        credsChecker.check(self.args.from_, password.decode('utf-8'))
        hashed_pass = hashlib.sha512(password)
        x = hashed_pass.hexdigest()
        json_format = {'gmail': self.args.from_,
                       'password': x}
        with open('pass.json', 'w+') as f:
            json.dump(json_format, f)
        print(f"{Fore.CYAN}[+]Saved the Email and Password")
        print("Sending Email Now")
        self.check_credentials()

    def check_credentials(self):
        if os.stat('pass.json').st_size != 0:
            with open('pass.json', 'r') as password_file:
                json_data = json.load(password_file)
                self.password = bytes(getpass.getpass(f'Enter Password for '
                                                      f'{Fore.BLUE}'
                                                      f' {self.args.from_}'
                                                      f'{Fore.RESET}:'),
                                      'utf-8')
                hashed = hashlib.sha512(self.password).hexdigest()
                if json_data['gmail'] == self.args.from_:
                    if str(json_data['password']) == str(hashed):
                        self.route()
                    else:
                        print(f'{Fore.RED}Wrong Password!{Fore.RESET}')
                        for i in range(1, 4):
                            self.password = bytes(
                                getpass.getpass(
                                    f'{Fore.RED}{i}{Fore.RESET}'
                                    f' Wrong Password Enter Again for '
                                    f'{Fore.BLUE}'
                                    f'{self.args.from_}{Fore.RESET}:'),
                                'utf8')
                            hashed = hashlib.sha512(self.password).hexdigest()
                            if json_data['password'] == str(hashed):
                                self.send_email_file()
                            else:
                                pass
                        sys.exit(f'{Fore.RED}Wrong Password')
                else:
                    self.new_email()
        else:
            self.new_email()

    def get_subject(self):
        try:
            subject_completer = AutoCompleter.MyCompleter(
                [greeting.strip() for greeting in
                 open('Autocompletions/greeting.txt', 'r').readlines()])
            readline.set_completer(subject_completer.complete)
            readline.parse_and_bind('tab: complete')
            return input(f'{Fore.BLUE}Subject>'
                         f'{Fore.RESET}') if self.args.subject else None
        except KeyboardInterrupt:
            sys.exit('\n' + "Exiting ! Did Not Send The Email.")

    def get_body(self):
        if self.args.body:
            try:
                print(f'{Fore.LIGHTBLACK_EX}Hint:{Fore.RESET} '
                      f'Press {Fore.BLUE}Ctrl+C{Fore.RESET} to '
                      'end the message!')
                while True:
                    line = input(f"{Fore.CYAN}Body>")
                    if line:
                        self.body_content_list.append(line)
                    else:
                        if line == "":
                            self.body_content_list.append("\n")
                        else:
                            break
                    self.body_content = '\n'.join(self.body_content_list)
            except KeyboardInterrupt:
                print(f"\n\n{Fore.LIGHTGREEN_EX}Body done!")
                return self.body_content

    def get_recipients(self):
        self.from_email = self.args.from_
        self.to_email = self.args.to

    def send_email_file(self):
        self.get_recipients()
        self.msg['subject'] = self.get_subject()
        self.msg['from'] = self.from_email
        self.msg['to'] = self.to_email
        text = MIMEText(self.getbody() if self.args.body else "", 'plain')
        self.msg.attach(text)
        if self.args.file:
            for file in self.args.file:
                with open(file, 'r') as f:
                    payload = MIMEBase('application', 'octet-stream')
                    payload.set_payload(f.read())
                    encoders.encode_base64(payload)
                    payload.add_header('Content-Disposition', 'attachment',
                                       filename=self.args.file
                                       [self.args.file.index(file)])
                    self.msg.attach(payload)
        try:
            if self.args.server is not None:
                self.server = self.args.server
            if self.args.port is not None:
                self.port = self.args.port
            with smtplib.SMTP(self.server, self.port) as session:
                session.starttls()
                session.login(self.from_email, self.password.decode())
                msg = self.msg.as_string()
                session.sendmail(self.from_email, self.to_email, msg)
        except smtplib.SMTPAuthenticationError:
            sys.exit(
                "Allow less secure apps is in the OFF state by going to  "
                "https://myaccount.google.com/lesssecureapps . "
                "Turn it on and try again. "
                "make sure the Sender email & password are correct.")
        except socket.gaierror:
            sys.exit(f"{Fore.RED}Check your internet & firewall settings.")
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{Fore.GREEN} Email Send ")
        sys.exit(0)

    def read_email(self):
        if self.args.imapserver is not None:
            self.imap_server = self.args.imapserver

        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
        except socket.gaierror:
            sys.exit(f"`{Fore.RED}{self.imap_server}{Fore.RESET}`"
                     " Service Not recogonised")
        self.get_recipients()
        mail.login(self.from_email, str(self.password.decode()))

        mail.select("INBOX", readonly=True)

        if self.args.search:
            self.search = f'(FROM "{self.args.search}")'
        _, selected_mails = mail.search(None, self.search)

        self.total_mails = len(selected_mails[0].split())

        print("Total Emails:", len(selected_mails[0].split()))

        if not self.args.listall:
            num_of_emails = selected_mails[0].split()[::-1][0:self.args.list]
        else:
            num_of_emails = selected_mails[0].split()[::-1]

        def verbose():
            print("\n===========================================")
            print(f"{Fore.MAGENTA}From:{email_message['from']}")
            print(f"{Fore.GREEN}To: {email_message['to']}")
            print(f"{Fore.BLUE}Subject:{email_message['subject']}")
            print(f"{Fore.RED}Date:{email_message['date']}")
            for part in email_message.walk():
                if part.get_content_type() == "text/plain" or "text/html":
                    message = part.get_payload(decode=True)
                    print("==========================================\n")
                    print(f"{message.decode()}")
                    print("==========================================\n")
                    break

        def concise():
            print("\n===========================================")
            print(f"{Fore.MAGENTA}From:{email_message['from']}")
            print(f"{Fore.BLUE}Subject:{email_message['subject']}")
            print(f"{Fore.RED}Date:{email_message['date']}")
            print("===========================================")

        print("Fetching...")

        for num in num_of_emails:
            _, data = mail.fetch(num, '(RFC822)')
            _, bytes_data = data[0]

            email_message = email.message_from_bytes(bytes_data)

            if self.args.verbose:
                verbose()
            else:
                concise()


if __name__ == '__main__':
    send = EmailSender()
