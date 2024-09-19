import yagmail
import schedule
import time
import datetime
import os

# Input your information by chnaging string part from here---------------------

email = 'your_account@gmail.com'
# used for email body (e.g. sincerely <myname>)
your_name = 'your_real_name'
recipient_name = 'John Doe'
# Your application password can be used only after 2-step verification
password = 'your_gmailpassword'

# Recipient's birthday information
today = datetime.date.today()
birthday_list = {
    # Change John to recipient's name
    "John": {
        # Change john@example.com into real recipient's email
        "email": "john@example.com",
        # Change Month and Day of a birthday
        "birthday": datetime.date(today.year, 12, 31),
        "attachment": "/path/to/john_card.pdf"  # Enter absolute path to a file if needed
        },
    "Jane": {
        "email": "jane@example.com",
        "birthday": datetime.date(today.year, 8, 22),
        "attachment": None  # 添付ファイルなし
        },
        # Add other recipient from here
    }
# If you want to change the content, modify below
subject = f"Happy birthday {recipient_name}!"
body = f"""Dear {recipient_name},

Wishing you a very happy birthday filled with love, laughter, and joy! May all your dreams and aspirations come true.
Looking forward to seeing you soon! Have a fantastic birthday!

Best wishes, {your_name}"""
# --------------------------------------------------------------------------^^^


