#!/usr/bin/env python3

import datetime
import time

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser

api_id = '<API ID>'
api_hash = '<API HASH>'
token = '<Bot Token>'

phone = '<e.g +0000000000>'


def send_message(msg):
    client = TelegramClient('session', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    try:
        receiver = InputPeerUser('user_id', 'user_hash')
        client.send_message(receiver, msg, parse_mode='html')
    except Exception as e:
        print(e)
    client.disconnect()


if __name__ == "__main__":
    while True:
        today = datetime.date.today()
        if today != datetime.date(2020, 10, 15):
            time.sleep(60 * 60 * 24)
        else:
            send_message("Happy Birth Day")
