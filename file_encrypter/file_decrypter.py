import pyAesCrypt
import sys
bufferSize = 64 * 1024
password = input("password for decrypting : ")
opname = sys.argv[1].replace(".aes", "")
try:
    pyAesCrypt.decryptFile(sys.argv[1], opname, password, bufferSize)
    print(f"FILE HAS BEEN DECRYPTED SUCCESSFULLY. STORED IN {opname}")
except ValueError:
    print("WRONG PASSWORD OR THE FILE IS CORRUPTED")
