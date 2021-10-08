# Discord Github Notifications Bot
This is a discord bot written in Python3 to send github notifications from a repo to a discord channel

# Build & Deploy

## Installation
The bot requires `discord` python module and other modules for working properly.

To install all of them we need to run

```python
pip3 install -r requirements.txt
```

## Configuration
To run the bot we need to make changes to config.py with our own configuration values.

`GITHUB_TOKEN`    - Your Github Token (Check Github https://github.com/settings/tokens/new)

`BOT_TOKEN`       - Discord Bot Token

`GITHUB_REPO`     - Github Repo in format `username/repo`

`GITHUB_USERNAME` - Your own Github Username

`DISCORD_CHANNEL` - Discord Channel to send notification

`command_prefix`  - Discord command front chararcter (`!` start)

`check_interval`  - Interval between notification checks (in minutes)


## Start
To start the bot we need to type

```python3 bot.py```


# Usage
The bot comes with these commands that control its behaviour.

* `!start`	- Starts to listen for notifications
* `!stop`	- Stops listening for notifications
* `!update`	- Check for notifications
