import yagmail
import datetime
import schedule
import time
import os
from typing import Optional

# Input your information by chnaging string part from here---------------------
# used for email body (e.g. sincerely <myname>)
your_name = "your_real_name"
your_email = "your_account@gmail.com"
# Your application password can be used only after 2-step verification
password = "your_gmailpassword"

# Enter recipient information below

birthday_list = {
    # Change John to recipient's name
    "John": {
        # Change john@example.com into real recipient's email
        "email": "john@example.com",
        # Change Year, Month and Day of a birthday
        "birthday": datetime.date(1995, 12, 31),
        # Enter an absolute path to attachement file
        "attachment": "/path/to/john_card.pdf",
    },
    "Jane": {
        "email": "jane@example.com",
        "birthday": datetime.date(2001, 8, 22),
        "attachment": None,  # 添付ファイルなし
    },  # Add other recipient from a below line
}
# -----------------------------------------------------------------------------


class BirthdaySender:
    """This automatically sends birthday wishes via Gmail."""

    def __init__(self, your_name, your_email, password) -> None:
        self.your_name = your_name
        self.sender_email = your_email
        self.birthday_list = birthday_list
        # for safer password storage
        yagmail.register(your_email, password)
        self.yag = yagmail.SMTP(your_email)

    def send_email(
        self, name: str, to_email: str, attachment_path: Optional[str] = None
    ) -> None:
        """Include attachement to email file if it is needed"""

        # If you want to change the content, modify below----------------------
        subject = f"Happy birthday {name}!"
        body = f"""Dear {name},

        Wishing you a very happy birthday filled with love, laughter, and joy!
        May all your dreams and aspirations come true.
        Looking forward to seeing you soon! Have a fantastic birthday!

        Best wishes, {self.your_name}"""
        # ---------------------------------------------------------------------

        email_params = {"to": to_email, "subject": subject, "contents": body}

        if attachment_path and os.path.exists(attachment_path):
            email_params["attachments"] = attachment_path
            print(f"{attachment_path} was included")

        try:
            self.yag.send(**email_params)
            print(f"Sent to {name}")
        except Exception as e:
            print(f"Failed to send email to {name}, Error: {e}")

    def send_email_if_birthday(self) -> None:
        """Call send_email if today is birthday"""
        today = datetime.date.today()

        for name, info in self.birthday_list.items():
            birthday = info["birthday"]
            if today.month == birthday.month and today.day == birthday.day:
                return self.send_email(name, info["email"], info["attachment"])

    def run(self):
        return self.send_email_if_birthday()


if __name__ == "__main__":
    birthday_sender = BirthdaySender(your_name, your_email, password)

    schedule.every().day.at("07:00").do(birthday_sender.run)

    while True:
        schedule.run_pending()
        time.sleep(1)
