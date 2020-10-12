#!/usr/bin/python3
# Created by Sam Ebison ( https://github.com/ebsa491 )
# If you have found any important bug or vulnerability,
# contact me pls, I love learning ( email: ebsa491@gmail.com )

"""
This is a simple password manager CLI program
based on https://github.com/python-geeks/Automation-scripts/issues/111
"""

import argparse
import sys
import os
import sqlite3
import base64
import signal
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

# The program data file.
FILENAME = ".pass.db"

# Cookie(canary) value
COOKIE = "===PASSWORDS==="

# For coloring the outputs
GREEN_COLOR = "\033[1;32m"
RED_COLOR = "\033[1;31m"
NO_COLOR = "\033[0m"


def main():
    """The main function of the program."""

    status, is_first = check_database()  # status{0|-1} is_first{True|False}

    if status == -1:
        # ERROR
        print(f"[{RED_COLOR}-{NO_COLOR}] Error in database connection...")
        sys.exit(1)

    if args.password == '' or args.password is None:

        # User didn't enter the password (argument)
        if is_first:

            # New user
            user_password = getpass("Enter a new password for the program> ")
            confirm = getpass("Confirm it> ")

            if user_password != confirm:
                # ERROR
                print(f"[{RED_COLOR}-{NO_COLOR}] Didn't match...")
                sys.exit(1)

            if new(user_password, COOKIE, '-', 0) != 0:
                # ERROR (Cookie didn't set)
                print(f"[{RED_COLOR}-{NO_COLOR}] Error in saving...")
                os.remove(FILENAME)
                sys.exit(1)

        else:

            user_password = getpass("Enter your user password> ")

            if check_password(user_password) != 0:
                # ERROR
                print(f"[{RED_COLOR}-{NO_COLOR}] Wrong password...")
                sys.exit(1)

    else:

        # We have the password here
        user_password = args.password

        if check_password(user_password) != 0:
            # ERROR
            print(f"[{RED_COLOR}-{NO_COLOR}] Wrong password...")
            sys.exit(1)

    prompt(user_password)


def check_database():
    """
    This function checks the database file.
    If everything was going OK returns 0, is_first{True|False}
    and if not returns -1, False.
    If is_first was True that means the program has run for the first time.
    """

    try:

        # If it was True that means the program has run for the first time
        is_first = False

        if not os.path.isfile(FILENAME):
            is_first = True

        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    password TEXT NOT NULL
                    );"""
            )

        return 0, is_first
    except Exception:
        return -1, False


def check_password(user_password):
    """
    This function checks the user password and will return two values {0|-1},
    0 means the password is correct,
    -1 means it's wrong.
    """

    try:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            # Fetches the cookie (canary) value
            row = cursor.execute(
                "SELECT * FROM passwords WHERE id=0;"
            ).fetchone()

            bin_user_password = str(user_password).encode('utf-8')

            if decrypt(bin_user_password, row[1]).decode('utf-8') == COOKIE:
                # The password is correct
                # because it can decrypt the encrypted cookie value
                return 0
            else:
                # The password can't decrypt the cookie value (Wrong)
                return -1
    except Exception:
        return -1


def prompt(user_password):
    """
    This function will be called after checking the password and database.
    It gives you a prompt for entering your commands.
    Valid commands are 'new', 'delete', 'show', 'exit'.
    """

    print("Commands: [new] [delete] [show] [exit]")

    try:
        cmd = input("Enter your command> ")
    except EOFError:
        print("\nBye...")
        sys.exit(0)

    if cmd.lower() == 'new':

        name = input("Where did you use this password for> ")
        password = input("Enter the new password to save> ")

        if new(user_password, name, password) == 0:

            # Row added
            print(f"[{GREEN_COLOR}+{NO_COLOR}] Successfully added...")
            prompt(user_password)

        else:

            # ERROR
            print(
                f"[{RED_COLOR}-{NO_COLOR}] Error while writing the password..."
            )
            prompt(user_password)

    elif cmd.lower() == 'delete':

        id_num = input("Which id? > ")
        confirm = input("Are you sure [Y/n]> ")

        if confirm.lower() == 'y':

            if delete(id_num) == 0:
                # Row deleted
                print(f"[{GREEN_COLOR}+{NO_COLOR}] Successfully deleted...")
            else:
                # ERROR
                print(f"[{RED_COLOR}-{NO_COLOR}] Error in deleting...")

        prompt(user_password)

    elif cmd.lower() == 'show':

        result = select_data(user_password)

        if result == -1:
            # ERROR
            print(f"[{RED_COLOR}-{NO_COLOR}] Error in selecting the data...")
        else:
            show_data(result)

        prompt(user_password)

    elif cmd.lower() == 'exit':

        print("Bye...")
        sys.exit(0)

    else:

        print("Command not found...")
        prompt(user_password)


def new(user_password, name, password, id_num=-1):
    """
    This function used for inserting new row to the database.
    It will return two values {0|-1},
    0 means the row has inserted successfully,
    -1 means there was an error.
    parameters are (in sort) =>
    ===================================
    user_password: The program password,
    name: The tag of the new password,
    password: The new password,
    OPTIONAL id_num: Will be used for specific id number.
    """

    try:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()

            if id_num == -1:

                # insert id auto-increment
                cursor.execute(
                    """INSERT INTO passwords(name, password) VALUES (
                            ?,?
                        );""",
                    [
                        encrypt(
                            str(user_password).encode('utf-8'),
                            str(name).encode('utf-8')
                        ),
                        encrypt(
                            str(user_password).encode('utf-8'),
                            str(password).encode('utf-8')
                        )
                    ]
                )

            else:

                # insert the given id number
                cursor.execute(
                    """INSERT INTO passwords(id, name, password) VALUES (
                            ?,?,?
                        );""",
                    [
                        id_num,
                        encrypt(
                            str(user_password).encode('utf-8'),
                            str(name).encode('utf-8')
                        ),
                        encrypt(
                            str(user_password).encode('utf-8'),
                            str(password).encode('utf-8')
                        )
                    ]
                )

        return 0
    except Exception:
        return -1


def delete(id_num):
    """
    It gets an id number and will delete it from the database.
    It will return two values {0|-1}
    0 means the row has deleted successfully,
    -1 means there was an error.
    """

    try:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM passwords WHERE id = ? AND name != ?;",
                [id_num, COOKIE]
            )

        return 0
    except Exception:
        return -1


def select_data(user_password):
    """
    This function gets the program password (user_password)
    and returns the passwords list.
    returning -1 means there was an error
    """

    try:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()

            # password => id, encrypted name and encrypted password
            passwords = cursor.execute("SELECT * FROM passwords;").fetchall()

            # result => id, decrypted name and decrypted password
            result = []

            for (id_num, name, password) in passwords:
                result.append(
                    (
                        id_num,
                        decrypt(
                            str(user_password).encode('utf-8'), name
                        ).decode('utf-8'),
                        decrypt(
                            str(user_password).encode('utf-8'), password
                        ).decode('utf-8')
                    )
                )

            return result
    except Exception:
        return -1


def show_data(result):
    """
    A function for printing the passwords.
    It gets the password list.
    """

    # the length of result must be more than 1
    # because of the cookie row (0, ===PASSWORDS===, -)
    if len(result) <= 1:
        # Empty
        print("\n\n====== Nothing ======\n\n")
    else:

        print("\n==============================\n")

        for (id_num, name, password) in result:
            if name != COOKIE:
                print(f"({id_num}) {name} {GREEN_COLOR}{password}{NO_COLOR}")

        print("\n==============================\n")


def encrypt(key, source, encode=True):
    """A function for encryption."""

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
    """A function for decrypting the encrypted datum."""

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


def exit_program(sig, frame):
    """For handling SIGINT signal."""

    print("\nBye...")
    sys.exit(0)


if __name__ == '__main__':
    global args  # The program arguments

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

    # Handle SIGINT (same as ^C) signal
    signal.signal(signal.SIGINT, exit_program)

    main()
