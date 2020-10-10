#!/usr/bin/python3
# Creted by Sam Ebison ( https://github.com/ebsa491 )

import argparse
import os
from getpass import getpass
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

# The program data file.
FILENAME = ".data.txt"


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
            print("Welcome to my PASSWORD MANAGER!")
            prompt()
    else:
        # We have the password here

        if os.path.isfile(FILENAME):
            # File exists (the user used the program before)
            # Check the password
            check_password(args.password)
        else:
            # File doesn't exist (it's the first time)
            # Ignore the password and welcome
            print("Welcome to my PASSWORD MANAGER!")
            prompt()


def prompt():
    pass


def check_password(password):
    with open(FILENAME, 'r') as data_file:
        data = decrypt(password, data_file.read())
        if data[:15] == '===PASSWORDS===':
            # Password is correct
            prompt()
        else:
            # Password is wrong
            input_password = getpass("Enter the password> ")
            check_password(input_password)


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
