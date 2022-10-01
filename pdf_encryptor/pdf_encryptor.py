import argparse
import getpass
import pyAesCrypt
import os
import sys


BUFFERSIZE = 64 * 1024


def parse_args():
    parser = argparse.ArgumentParser(description="Encrypt "
                                     "and decrypt PDF files")
    parser.add_argument('-e', '--encrypt', dest='encrypt', type=str,
                        nargs=1, metavar='filename', help='Encrypt')
    parser.add_argument('-d', '--decrypt', dest='decrypt', type=str,
                        nargs=1, metavar='filename', help='Decrypt')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return args


def file_exist(filename):
    """
    Check to see if the entered file exists or not.
    """
    if not os.path.exists(filename):
        print("Error: '{}' does not exist".format(filename))
        sys.exit()


def encrypt(filename, password):
    """
    Function to generate the encrypted file.
    """
    pyAesCrypt.encryptFile(filename, f"{filename}.aes", password, BUFFERSIZE)


def decrypt(filename, password):
    """
    Function to decrypt the provided file.
    """
    output = filename.replace(".aes", "")
    try:
        pyAesCrypt.decryptFile(filename, output, password, BUFFERSIZE)
    except ValueError:
        print("Wrong password (or file is corrupted).")
        sys.exit()


if __name__ == '__main__':
    args = parse_args()
    if args.encrypt:
        encrypt_file = args.encrypt[0]
        file_exist(encrypt_file)
        password = getpass.getpass("Please provide the password to "
                                   "encrypt the file with: ")
        encrypt(encrypt_file, password)
        print("{} has been successfully encrypted.".format(encrypt_file))
    else:
        decrypt_file = args.decrypt[0]
        file_exist(decrypt_file)
        password = getpass.getpass("Please provide the password to "
                                   "decrypt the file with: ")
        decrypt(decrypt_file, password)
        print("{} has been successfully decrypted.".format(decrypt_file))
