import os
import smtplib
import tweepy
from check_upcoming_ex_dividend import checkForUpcomingExDividend

# SECRETS
API_KEY = os.environ.get('APPLEREITNEWS_API_KEY')
API_SECRET = os.environ.get('APPLEREITNEWS_API_SECRET')
ACCESS_TOKEN = os.environ.get('APPLEREITNEWS_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('APPLEREITNEWS_ACCESS_TOKEN_SECRET')

# AUTHORIZATION
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    tweet_text = checkForUpcomingExDividend()
    # MAKE TWEET
    if tweet_text == False:
      print("Ex-Dividend is not upcoming")
    else:
      api.update_status(tweet_text)
except Exception as ex:
    print(f'Could not execute due to: {ex}')
