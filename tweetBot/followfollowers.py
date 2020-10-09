#!/usr/bin/env python3

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

'''
A lot of Twitter API endpoints use pagination to return their results.
Tweepy cursors take away part of the complexity of working with paginated results.
The Cursor object is iterable and takes care of fetching the various result pages transparently.
'''


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()


"""
The Bot gets list of followers every minutes (adjustable within time.sleep param)
and iterate through it to follow user who are not already followed.
"""


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
