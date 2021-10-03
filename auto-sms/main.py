# Created by @advaitasaha
# Imports
import requests

# Variables
global apiKey
global SID
global senderID
apiKey = ""  # enter your api key
SID = ""  # enter your SID number
senderID = ""  # enter the senderID registered

# Functions for semding SMS


def send_sms(number):

    headers_sms = {
        "api-key": apiKey,
    }

    data_sms = {
        "type": "TXN",
        "to": "+91{}".format(str(number)),
        "sender": senderID,
        "source": "API",
        "body": "Thank you {} for using this software.".format(
            "name"
        ),  # change the body of the messages
        "template_id": "1207161891861378858",  # enter registered template id
    }

    response = requests.post(
        "https://api.kaleyra.io/v1/{}/messages".format(SID),
        headers=headers_sms,
        data=data_sms,
    )
    return response.json()


def number_val(number):

    headers = {
        "Content-Type": "json",
        "api-key": apiKey,
    }

    response = requests.get(
        "https://api.kaleyra.io/v1/{}/lookup/+91{}".format(SID, str(number)),
        headers=headers,
    )
    if response.json()["invalid_count"]:
        return False, response.json()
    else:
        return True, response.json()


def send_flash_sms(number):

    headers = {
        "api-key": apiKey,
    }

    data = {
        "to": "+91{}".format(str(number)),
        "type": "TXN",
        "sender": senderID,
        "body": "Thank you {} for using this software.".format(
            "name"
        ),  # change the body of the messages
        "flash": "1",
    }

    response = requests.post(
        "https://api.kaleyra.io/v1/{}/messages".format(SID), headers=headers, data=data
    )
    return response.json()


while True:
    print("------------------------------------------------------------------")
    print("Welcome to Kaleyra SMS sending software, created by @Advaita Saha")
    print("------------------------------------------------------------------")
    print("1: Send SMS")
    print("2: Send flash SMS")
    print("3: Check Number Validity")
    print("0: Exit Program")
    print("------------------------------------------------------------------")
    userInput = int(input("Enter the option number you want to perform: "))

    if userInput == 1:
        number = int(input("Enter the phone number to which you want to send: "))
        out = send_sms(number)
        print("------------------------------------------------------------------")
        print("SMS sent, below is the JSON output")
        print(out)

    elif userInput == 2:
        number = int(input("Enter the phone number to which you want to send: "))
        out = send_flash_sms(number)
        print("------------------------------------------------------------------")
        print("Flash SMS sent, below is the JSON output")
        print(out)

    elif userInput == 3:
        number = int(input("Enter the phone number to which you want to send: "))
        out = number_val(number)
        if out[0]:
            print("------------------------------------------------------------------")
            print("Valid Number, details below")
            print(out[1])
        else:
            print("------------------------------------------------------------------")
            print("Invalid Number")
            print(out[1])

    elif userInput == 0:
        break
