import sys

from pyrogram import Client

api_id = None
api_hash = None

with Client("my_account", api_id, api_hash) as app:
    for file in sys.argv[1:]:
        app.send_document("me", file)
        print(f'[+] Successfully uploaded {file}.')
