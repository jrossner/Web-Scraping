import os
import tweepy
from get_actual_earnings import checkEarningsFigures

# SECRETS
API_KEY = f"{os.environ.get('API_KEY')}"
API_SECRET = f"{os.environ.get('API_SECRET')}"
ACCESS_TOKEN = f"{os.environ.get('ACCESS_TOKEN')}"
ACCESS_TOKEN_SECRET = f"{os.environ.get('ACCESS_TOKEN_SECRET')}"

# AUTHORIZATION
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    tweet_text = checkEarningsFigures()
    if tweet_text == False:
      print("Actual Earnings not posted yet")
    else:
      # MAKE TWEET
      api.update_status(tweet_text)
except Exception as ex:
    print(f'Could not execute due to: {ex}')
