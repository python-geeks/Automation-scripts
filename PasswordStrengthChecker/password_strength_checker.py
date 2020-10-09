import sys
import re

password = sys.argv[1]
regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')

t1 = len(password) >= 8
t2 = not (regex.search(password) is None)
t3 = any(c.islower() for c in password)
t4 = any(c.isupper() for c in password)
t5 = any(c.isdigit() for c in password)

if t1 and t2 and t3 and t4 and t5:
    print("Password is STRONG")
else:
    print("Password is WEAK")
