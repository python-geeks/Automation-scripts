import tweepy
from time import sleep
# Import your keys from keys.py present in the same folder
from keys import consumer_key
from keys import consumer_secret
from keys import access_token
from keys import access_token_secret


def retweet(hashtag, retweetNum):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Input your hashtag during main function call
    # Input number of retweets during main function call
    for tweet in tweepy.Cursor(api.search, q=hashtag).items(retweetNum):
        try:
            print('\nTweet found by @' + tweet.user.screen_name)
            print('Attempting to retweet')
            tweet.retweet()
            print('Retweet published successfully.')
            # Change time for sleep accordingly.
            sleep(10)
        # Reasons why your retweet failed
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)
        except StopIteration:
            break


def main():
    print("Tell me a hashtag to retweet: ")
    hashtag = input()
    hashtag = '#' + hashtag
    print("Tell me how many times do I retweet: ")
    retweetNum = int(input())
    print("Retweet process started")
    retweet(hashtag, retweetNum)


if __name__ == '__main__':
    main()
