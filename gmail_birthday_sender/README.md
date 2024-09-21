# Gmail Birthday Sender

This script automatically sends birthday wishes via Gmail.
You just need to enter your information at beginning.

> [!WARNING]
> This script lacks strong security for your email

## Requirements

- Python 3

## Instructions

1. Create google account
2. Turn on [2-Step Verification](https://support.google.com/accounts/answer/185839)
3. Create [an application password](https://support.google.com/accounts/answer/185833#zippy=%2Cremove-app-passwords)

### Enter your information in `main.py`

- Enter your gmail account, your name and application password

```py
your_name = "your_real_name"
your_email = "your_account@gmail.com"
password = "your_gmailpassword"
```

- Enter recipient's information here

```py
    # Change John to recipient's name
    "John": {
        # Change john@example.com into real recipient's email
        "email": "john@example.com",
        # Change Month and Day of a birthday
        "birthday": datetime.date(1995, 12, 31),
```

(Example)
Name: John
Email: john@example.com,
Year, Month and Day of a birthday: 1995, 12, 31

- Enter absolute path to a attachement file if you want

```py
        "attachment": "/path/to/john_card.pdf"
        },
```

If you don't need, write `None` instead

```py
        "attachment": None
```

- If you want to change the subject and body of email, modify below string

```py
        subject = f"Happy birthday {name}!"
        body = f"""Dear {name},

        Wishing you a very happy birthday filled with love, laughter, and joy!
        May all your dreams and aspirations come true.
        Looking forward to seeing you soon! Have a fantastic birthday!

        Best wishes, {self.your_name}"""
```

### Run the script

After you're done installing Python and pip, run the following command from your terminal to install the requirements from the same folder (directory) of the project.

```bash
pip install -r requirements.txt
```

After satisfying all the requirements for the project, Open the terminal in the project folder and run

```bash
python dictionary.py
```

or

```bash
python3 dictionary.py
```
