# Zip Password Cracker

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

Attempts to brute force the password of a zip file.
How to user:
```
python3 zip_password_cracker.py --zip <zip file> --passwords <file with passwords>
```
If no dictionary file is passed, it will use the passwords.txt file instead.

password.txt Sources: https://github.com/danielmiessler/SecLists/
Got from there file with 10k most common credentials.

**You will get passwords.txt file [here](https://gist.github.com/pawangeek/c96476f5d7e874e888748ef73cd1a6f7)**
