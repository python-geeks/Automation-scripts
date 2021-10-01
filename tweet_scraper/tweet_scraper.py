import os
import tweepy


username = "saranshchopra7"    # edit the username here
number_of_tweets = 100  # max can be 200

# API keys
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# auth and API objects
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# scrape tweets
tweets = api.user_timeline(
    screen_name=username, count=number_of_tweets, tweet_mode="extended"
)

file = open("tweets.txt", "a", encoding="utf-8")

# store the tweets
for tweet in [tweet.full_text for tweet in tweets]:
    file.write(
        tweet + "\n===============================================================\n"
    )

file.close()
