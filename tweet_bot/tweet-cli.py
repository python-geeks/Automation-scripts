#!/usr/bin/env python3
import tweepy
import json
import sys
from config import create_api

usage = """
usage:
                    tweet-cli "Tweet Text"
example:
                    tweet-cli "tweeting using tweet -cli interface"
"""

def tweet_cli(api):
    if not len(sys.argv) == 2:
        print(usage)
    else:
        api.update_status(sys.argv[1])