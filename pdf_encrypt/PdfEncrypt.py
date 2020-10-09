import pyAesCrypt
import sys
import re

bufferSize = 64 * 1024


def check_password(password):
    """
    function to check the strength of password
    """
    regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')

    t1 = len(password) >= 8
    t2 = not (regex.search(password) is None)
    t3 = any(c.islower() for c in password)
    t4 = any(c.isupper() for c in password)
    t5 = any(c.isdigit() for c in password)

    if t1 and t2 and t3 and t4 and t5:
        return True
    else:
        return False


password = input("password for encrypting : ")
password_strength = check_password(password)

while not password_strength:
    print("WEAK Password")
    print("Please enter a strong password")
    password = input("password for encrypting : ")
    password_strength = check_password(password)

pyAesCrypt.encryptFile(sys.argv[1], f"{sys.argv[1]}.aes", password, bufferSize)
print(f"FILE HAS BEEN ENCRYPTED SUCCESSFULLY. STORED IN {sys.argv[1]}.aes")
