from telethon import TelegramClient, events
from telethon.tl.functions.messages import ForwardMessagesRequest





api_id = <Your Telegram API ID>
api_hash = 'Your Telegram Hash ID'
client = TelegramClient('anon', api_id, api_hash)
@client.on(events. NewMessage(outgoing=False))
async def handler(event): 
    chat_id = event.chat_id
    # Let's print all the chat ids you are incoming messages from
    print(chat_id)
    #If you just want to get messages from 1 chat just remove the or statement after the 1st one
    if chat_id ==<Chat Id of the origin message Here> or chat_id==<Chat Id of the origin message Here> or chat_id==<Chat Id of the origin message Here>:
        msg = event.raw_text
        await client. send_message(<Chat Id of of the Chat Where To Send>,msg)

 
 
client.start()
client.run_until_disconnected()