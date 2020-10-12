import smtplib
import argparse
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender(object):
    def __init__(self, host="localhost", port=25, username=None,
                 password=None):
        self.host = host
        self.port = port
        # we can have no username/password but no host or port
        self.username = username or None
        self.password = password or None
        # setup logging
        logging.basicConfig(
            format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
            level=logging.INFO)
        self.logger = logging.getLogger('EmailSender')

    def email_message_input(self):
        """initialises a keyboard based prompt to users of the command line
        script to generate the email message content used to send to the
        recipient.

        :return: object contain the email message provided by the user
        """
        try:
            self.logger.info("Enter/Paste your email. Ctrl-D or Ctrl-Z "
                             "to save it")
            contents = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                contents.append(line)

            return '\n'.join(contents)
        except Exception as e:
            self.logger.error(f"Unable to process email message input: {e}")
            raise Exception("Unable to process email message input")

    def prepare_email(self, subject, from_email, to_email, body):
        """Takes the subject, from_email, to_email and message and generates
        a MIME formatted email.

        :param subject: Mail subject
        :param from_email: Mail from email address
        :param to_email: Mail recipient address
        :param body: Message to send to recipient

        :return: MIME formatted email as a string
        """
        try:
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to_email
            msg.attach(MIMEText(body, 'plain'))

            return msg.as_string()
        except Exception as error:
            self.logger.error(f"Unable to prepare email message: {error}")
            raise Exception("Unable to prepare email message")

    def send_email(self, subject, from_email, to_email, msg,
                   host=None, port=None, username=None, password=None):
        """Sends an email, has the options for host, port, user/pass so you can
        choose where to send an email.

        :param host: SMTP server hostname or IP
        :param port: SMTP server post
        :param username: Mail account username
        :param password: Mail account password (sent using starttls())
        :param subject: Mail subject
        :param from_email: Mail from email address
        :param to_email: Mail recipient address
        :param msg: Message to send to recipient

        :return: smtp sendmail response
        """
        try:
            host = host or self.host
            port = port or self.port
            username = username or self.username
            password = password or self.password

            self.logger.info(f"Setting up connection to smtp://{host}:{port}")

            smtp = smtplib.SMTP(host, port)
            smtp.ehlo()
            smtp.starttls()

            if username and password:
                smtp.login(username, password)

            email = self.prepare_email(subject, from_email, to_email, msg)

            self.logger.info(f"Sending email to: {to_email}")
            return smtp.sendmail(from_email, to_email, email)
        except ConnectionRefusedError:
            self.logger.error(f"Error to connect to smtp://{host}:{port}")
            raise Exception(f"Error to connect to smtp host: "
                            f"smtp://{host}:{port}")
        except Exception as error:
            self.logger.error(f"Unable to send email message: {error}")
            raise Exception("Unable to send email message")


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="EmailSender")
    args.add_argument('--subject', help="Subject to use in the Email message",
                      required=True)
    args.add_argument('--from_email', help="Email address to use as the from"
                                           " address.", required=True)
    args.add_argument('--to_email', help="Email address to used to send emails"
                                         " too.", required=True)
    args.add_argument('--msg', help="Email message", default=None)
    args.add_argument('--host', help="SMTP Host", default="localhost")
    args.add_argument('--port', help="SMTP Port", default=25, type=int)
    args.add_argument('--username', help="SMTP username", default=None)
    args.add_argument('--password', help="SMTP password", default=None)
    args = args.parse_args()

    try:

        # create the EmailSender class object, using the command line options
        # as params
        email_sender = EmailSender(host=args.host,
                                   port=args.port,
                                   username=args.username,
                                   password=args.password)

        # set the message to the message provided in the command line options
        # if specified, otherwise ask for input
        if args.msg:
            msg = args.msg
        else:
            email_sender.logger.info("Email message not provided, please "
                                     "input now!")
            msg = email_sender.email_message_input()

        # send the email
        email_sender.send_email(subject=args.subject,
                                from_email=args.from_email,
                                to_email=args.to_email,
                                msg=msg)

        email_sender.logger.info("Email message successfully delivered")
    except Exception as e:
        email_sender = EmailSender()
        email_sender.logger.error(f"Unable to execute the EmailSender "
                                  f"commandline script: {e}")
