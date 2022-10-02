# this = b'hello'
# print(this)
# print(this.decode())
import hashlib
import codecs

password = b"gautam<21>"
hashed_pass = hashlib.sha512(password)
x = hashed_pass.hexdigest()
print(x)