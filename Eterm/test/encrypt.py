import hashlib
import sys


def check():
    if open('../src/pass.json', 'r').read():  # password already there
        pass
    else:
        password = bytes(input('Enter Your Password:'), 'utf-8')
        with open('../src/pass.json', 'w+') as f:
            f.write(str(hashlib.sha512(password).digest()))


def get_pass():
    password = bytes(input("Enter Password:"), 'utf-8')
    hashed = hashlib.sha512(password).digest()
    real_pass = open('../src/pass.json', 'r').readline().strip()
    if str(hashed) == str(real_pass):
        print("nc")
    else:
        sys.exit("Wrong Password")


check()
