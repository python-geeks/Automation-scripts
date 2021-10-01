import os
import sys
import csv
import pyperclip
import re

# Create phone regex.
phoneRegex = re.compile(
    r'''(\(?([\d]{3})\)?[\.|\s|\-]*([\d]{3})[\.|\s|\-]*([\d]{4}))''',
    re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-] + #username
    @                   # @symbole
    [a-zA-Z0-9.-] +     # domain
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

text = ""

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        text = source_file.read()
        source_file.close()
    # Failikng if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No file, no usage
else:
    print("Usage: extract-email-phone.py <source_file.txt>")

phoneMatches = []
emailMatches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[2], groups[3]])
    phoneMatches.append(phoneNum)
for groups in emailRegex.findall(text):
    emailMatches.append(groups[0])

if (len(phoneMatches) > 0 or len(emailMatches)):
    matches = '\n'.join(phoneMatches) + '\n' + '\n'.join(emailMatches)
    pyperclip.copy(matches)
    print('Copied to clipboard!')
    s = pyperclip.paste()
    print("Phone Numbers - \n\t"
          + '\n\t'.join(phoneMatches)
          + "\nEmails - \n\t"
          + '\n\t'.join(emailMatches))

    with open('phones.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows([phoneMatches])
        print("Phone numbers saved to phones.csv")

    with open('emails.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows([emailMatches])
        print("Phone numbers saved to emails.csv")
else:
    print('No phone numbers or email addresses found.')
