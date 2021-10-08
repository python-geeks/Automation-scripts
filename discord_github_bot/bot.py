from discord.ext.commands import Bot
from discord.utils import get as discord_get
from discord.ext.tasks import loop
import discord
import requests
import json

# config
import config
github_session = requests.Session()
github_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)
# This keeps the already sent notification ids
already_sent = []

# Discord Bot Client
client = Bot(command_prefix=config.command_prefix)


# Gets Notifications from Github
def get_github_notifications():
    url = f'https://api.github.com/repos/{config.GITHUB_REPO}/notifications'
    r = github_session.get(url)
    return r.text


# Notification Sender function
async def send_notification(context):
    # Check if channel is present in guild
    global already_sent
    channel = discord_get(
        context.guild.text_channels,
        name=config.DISCORD_CHANNEL,
    )
    if channel is None:
        # else use the context
        print(f'[Notifications] Cannot find channel {config.DISCORD_CHANNEL}\n')
        channel = context
    try:
        notifications = get_github_notifications()
        notifications = json.loads(notifications)
    except Exception as err:
        print(f'Exception Occured. {str(err)}')
        notifications = None
    if notifications is None:
        if context.message:
            await context.message.reply
        else:
            await context.guild.send("There was some error in getting notifications....\nTry Later.")
        return
    # Loop through notifications and check if already sent
    for notifi in notifications:
        if notifi["id"] in already_sent[:100]:
            break
        # Log Current Notification to Console
        print(f'[Notification] ID: {notifi["id"]}')
        print(f'[Notification] Title: {notifi["subject"]["title"]}')
        print(f'[Notification] Updated At: {notifi["updated_at"]}')
        print(f'[Notification] URL: {notifi["subject"]["url"]}')
        # Get URL to the notification subject
        direct_url = str(notifi["subject"]["url"]).replace("api.github", "github").replace("/repos/", "/")
        # Make a new message and send it
        embededMessage = discord.Embed(
            title=f'{notifi["id"]} - {notifi["subject"]["title"]}',
            url=direct_url,
            description=f'Reason: {notifi["reason"]}\nUpdated At: {notifi["updated_at"]}\nURL: {direct_url}',
            color=discord.Color.blue())
        # Add the notification ID to list of already sent, so it does'nt repeat
        already_sent.insert(0, notifi["id"])
        await channel.send(embed=embededMessage)
    return


# Discord Bot Connected
@client.event
async def on_ready():
    print(f'{client.user} has connected!')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name='Type !help to get help'
        )
    )


# Runs on !update command
@client.command(name='update')
async def update(context):
    print("[Command] Updating Notifications.....")
    await context.message.reply(
        "Fetching Github Notification Updates (if any), Please Wait...."
    )
    await send_notification(context)


# Runs on !start command
@client.command(name='start')
async def start_notifications(context):
    print("Starting Notifications Bot....")
    notify.start(context)
    await context.message.reply("Starting Notifications Bot....")


# Runs on !stop command
@client.command(name='stop')
async def stop_notifications(context):
    print("[Command] Notifications Bot Has Stopped....")
    notify.cancel()
    await context.message.reply("Notifications Bot Has Stopped....")


# Run Notification checks in discord.task.loop
@loop(minutes=config.check_interval)
async def notify(context):
    print("[Auto] Updating Notifications.....")
    await send_notification(context)


# Run the Discord Client Bot
client.run(config.BOT_TOKEN)
