#!/usr/bin/env python3
from sys import argv
import tweepy
import json
import sys
from config import create_api

usage = """
usage:
                    tweet-cli "Tweet Text"
example:
                    tweet-cli "this is my tweet from tweet-cli"
"""


def tweet_cli(api):
    if not len(sys.argv) == 2:
        print(usage)
    else:
        api.update_status(sys.argv[1])


if __name__ == "__main__":
    api = create_api()
    tweet_cli(api)

