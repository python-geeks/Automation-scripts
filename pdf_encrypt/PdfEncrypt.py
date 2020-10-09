import pyAesCrypt
import sys
bufferSize = 64 * 1024
password = input("password for encrypting : ")
pyAesCrypt.encryptFile(sys.argv[1], f"{sys.argv[1]}.aes", password, bufferSize)
print(f"FILE HAS BEEN ENCRYPTED SUCCESSFULLY. STORED IN {sys.argv[1]}.aes")
