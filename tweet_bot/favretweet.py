#!/usr/bin/env python3

import tweepy
import logging
from config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

"""
Resuable api object from config.py.
Tweepy to uses sub-classes of tweepy objects within FavRetweetListener class.
Tweepy stream to actively watch for tweets that contain certain keywords.
For each tweet, if you’re not the tweet author, it will mark the tweet as Liked and then retweet it.
"""


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    # If the tweet is a reply or not from me it will ignore it.
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        """
        This is like a maker, this is coming from tweepy favorited class.
        If it did not favorited(Smiliary like) the tweet yet, it will favorited it if not it returns an error.
        Try/Except is necessary to handling possible Errors.
        """
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception:
                logger.error("Error on fav", exc_info=True)
        """
        A similar case like favorited class.
        If it did not retweeted the tweet yet, it will retweeted it if not it returns an error.
        Try/Except is necessary to handling possible Errors.
        """
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception:
                logger.error("Error on fav and retweet", exc_info=True)

    # Logger for errors.
    def on_error(self, status):
        logger.error(status)


"""
The main uses a stream to filter tweets that contain the words of a list as keywords parametrs.
Bellow we used ["Python", "Tweepy", "Hacktoberfest"]
"""


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["Python", "Tweepy", "Hacktoberfest"])
