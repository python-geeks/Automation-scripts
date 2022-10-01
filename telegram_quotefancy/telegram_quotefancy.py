# ----- imports -----
import time
import schedule
import requests
from quotefancy import get_quote

# Some Required Vars
BOT_TOKEN = ""  # Your Telegram Bot's Token. @BotFather
CHAT_IDS = []  # list of chat Id, where it should send posts.

if not BOT_TOKEN:
    BOT_TOKEN = input("Enter Your Telegram BOT Token\n---> ")

if not CHAT_IDS:
    CHAT_IDS = input(
        "\nEnter Chat Ids where to send Quotes."
        + " (seperate by space for more than 1) : \n----> "
    )
    CHAT_IDS = [int(chat) for chat in CHAT_IDS.split(" ")]

BASE_URI = f"https://api.telegram.org/bot{BOT_TOKEN}/"


def post_quote_to_telegram():
    "function that will post QuoteFancy Quotes to Telegram"

    for chat in CHAT_IDS:
        post_url = get_quote(type="img")
        json_data = {"chat_id": chat, "photo": post_url}
        post_url = BASE_URI + "sendPhoto"

        # Calling Telegram Methods
        content = requests.post(post_url, json=json_data).json()
        if not content["ok"]:
            print(
                f"ERROR : {content['error_code']} :"
                + f"{content['description']} - {chat}"
            )
        else:
            print(f"Posted Quote in {chat}!")


# You can Choose Gap Interval by self here..
schedule.every().day.at("00:00").do(post_quote_to_telegram)

print("Started Successfully...")

# looping Scheduler's Task

while True:
    schedule.run_pending()
    time.sleep(5)
