# Tweet Scrapper

A script that scrapes the latest x tweets from a given Twitter account.

## Requirements
1. Libraries listed in `requirements.txt`
2. Twitter Developer Account - [here](https://developer.twitter.com/)

## Usage
1. Add your Twitter Developer Credentials as environment variables
```bash
$ export CONSUMER_KEY="<Cosumer Key>"
$ export CONSUMER_SECRET="<Consumer Secret>"
$ export ACCESS_TOKEN="<Access Token>"
$ export ACCESS_TOKEN_SECRET="<Access Token Secret>"
```
1. Change the `username` and the `number_of_tweets` in `tweet_scraper.py`
2. Run the script `python tweet_scraper.py`
