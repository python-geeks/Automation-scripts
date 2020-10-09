#!/usr/bin/python3
# Creted by Sam Ebison ( https://github.com/ebsa491 )

import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

# The program data file.
FILENAME = ".data.txt"


def main():
    pass


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
    main()
