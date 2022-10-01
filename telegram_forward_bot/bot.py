from telethon import TelegramClient, events
# from telethon.tl.functions.messages import ForwardMessagesRequest
api_id = 111111
# Replace 111111 with Your Telegram API ID
api_hash = 'Your Telegram Hash ID'
client = TelegramClient('anon', api_id, api_hash)


@client.on(events. NewMessage(outgoing=False))
async def handler(event):
    chat_id = event.chat_id
# Let's print all the chat ids you are incoming messages from
    print(chat_id)
    if chat_id == 22222:
        # Replace 22222 with the Chat Id of the origin message Here
        msg = event.raw_text
        await client. send_message(44444, msg)
# Replace 44444 with the Chat Id of of the Chat Where To Send
client.start()
client.run_until_disconnected()
