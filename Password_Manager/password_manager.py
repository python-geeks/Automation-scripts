#!/usr/bin/python3
# Creted by Sam Ebison ( https://github.com/ebsa491 )

import argparse
import sys
import os
from getpass import getpass
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

# The program data file.
FILENAME = ".data.txt"
GREEN_COLOR = "\033[1;32m"
RED_COLOR = "\033[1;31m"
NO_COLOR = "\033[0m"


def main():

    if args.password == '' or args.password is None:
        # User didn't enter the password

        if os.path.isfile(FILENAME):
            # File exists (the user used the program before)
            # Ask the password
            # secret prompt for entering the password
            password = getpass("Enter the password> ")
            check_password(password)
        else:
            # File doesn't exist (it's the first time)
            # Welcome
            welcome()
    else:
        # We have the password here

        if os.path.isfile(FILENAME):
            # File exists (the user used the program before)
            # Check the password
            check_password(args.password)
        else:
            # File doesn't exist (it's the first time)
            # Ignore the password and welcome
            welcome()


def welcome():
    print("Welcome to my PASSWORD MANAGER!")
    prompt()


def prompt():
    passwords = show()

    if passwords == -1:
        print(f"[{RED_COLOR}-{NO_COLOR}] Can't show the passwords...")
        sys.exit(1)

    print_passwords(passwords)

    print("Commands: [new] [delete] [show] [exit]")
    cmd = input("Enter your command> ")

    if cmd.lower() == 'new':

        name = input("Where did you use this password for> ")
        password = input("Enter the new password> ")

        if new(passwords.count, name, password) == 0:
            print(f"[{GREEN_COLOR}+{NO_COLOR}] Successfully added...")
            prompt()
        else:
            print(
                f"[{RED_COLOR}-{NO_COLOR}] Error while writing the password..."
            )
            prompt()

    elif cmd.lower() == 'delete':

        id_num = input("Which id? > ")
        confirm = input("Are you sure [Y/n]> ")

        if confirm.lower() == 'y':
            if delete(id_num) == 0:
                print(f"[{GREEN_COLOR}+{NO_COLOR}] Successfully deleted...")

        prompt()

    elif cmd.lower() == 'show':

        passwords = show()
        print_passwords(passwords)
        prompt()

    elif cmd.lower() == 'exit':
        sys.exit(0)
    else:
        print("Command not found...")
        prompt()


def new(id_num, name, password):
    try:
        with open(FILENAME, 'a') as data_file:
            name = str(name).replace('\n', '')
            password = str(password).replace('\n', '')
            data_file.write(f"{id_num}\t{name}\t{password}")
            return 0
    except Exception:
        return -1


def delete(id_num):
    try:
        with open(FILENAME, 'r') as data_file:
            lines = data_file.readlines()
        with open(FILENAME, 'w') as data_file:
            for line in lines:
                if line.strip("\n").split("\t")[0] != str(id_num):
                    data_file.write(line)
            return 0
    except Exception:
        return -1


def show():
    try:
        with open(FILENAME, 'r') as data_file:
            # *[1:] => Ignore the first line ('===PASSWORDS===')
            return data_file.readlines()[1:]
    except Exception:
        return -1


def print_passwords(passwords):
    for password in passwords:
        properties = password.split('\t')
        print(f"{properties[0]} => {properties[1]}, {properties[2]}")


def check_password(password):
    try:
        with open(FILENAME, 'r') as data_file:
            data = decrypt(password, data_file.read())
            if data[:15] == '===PASSWORDS===':
                # Password is correct
                prompt()
            else:
                # Password is wrong
                input_password = getpass("Wrong, Enter again> ")
                check_password(input_password)
    except Exception:
        print(f"[{RED_COLOR}-{NO_COLOR}] ERROR...")
        sys.exit(1)


def encrypt(key, source, encode=True):

    # use SHA-256 over our key to get a proper-sized AES key
    key = SHA256.new(key).digest()

    # generate iv
    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)

    # calculate needed padding
    padding = AES.block_size - len(source) % AES.block_size

    # Python 2.x: source += chr(padding) * padding
    source += bytes([padding]) * padding

    # store the iv at the beginning and encrypt
    data = iv + encryptor.encrypt(source)
    return base64.b64encode(data).decode("utf-8") if encode else data


def decrypt(key, source, decode=True):

    if decode:
        source = base64.b64decode(source.encode("utf-8"))

    # use SHA-256 over our key to get a proper-sized AES key
    key = SHA256.new(key).digest()

    # extract the IV from the beginning
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)

    # decrypt
    data = decryptor.decrypt(source[AES.block_size:])

    # pick the padding value from the end; Python 2.x: ord(data[-1])
    padding = data[-1]

    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")

    # remove the padding
    return data[:-padding]


if __name__ == '__main__':
    global args

    parser = argparse.ArgumentParser(description="Password Manager CLI")
    # -p | --password PASSWORD
    parser.add_argument(
        '-p',
        '--password',
        metavar='password',
        type=str,
        default='',
        help='the program password'
    )
    args = parser.parse_args()

    main()
