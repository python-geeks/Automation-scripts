import os
import sys
import json
import time
import requests
from win10toast import ToastNotifier


def check_availability():
    # check if the running device is windows
    if os.name == 'nt':
        pass
    else:
        print('This script only runs on windows.')
        sys.exit(0)


def get_quote():
    # access api to get a quote
    url = 'https://zenquotes.io/api/random'
    req = requests.request('GET', url)

    if req.status_code != 200:
        print('Connot reach api.')
        sys.exit(0)
    else:
        pass

    data = json.loads(req.content)
    # pprint(data)
    return data


def create_notifier(data):
    quote = data[0]['q']
    author = data[0]['a']
    toast = ToastNotifier()
    toast.show_toast(f"By {author}", quote)


def main_app():
    time_ = int(input('Repeat notification after (hours): '))
    while True:
        check_availability()
        data = get_quote()
        create_notifier(data)
        print('Sent notification.')
        time.sleep(time_ * 3600)


if __name__ == '__main__':
    main_app()
