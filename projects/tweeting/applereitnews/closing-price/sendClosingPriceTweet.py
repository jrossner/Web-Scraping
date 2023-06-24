import os
import tweepy
from get_closing_price import getClosingPrice

# SECRETS
API_KEY = f"{os.environ.get('API_KEY')}"
API_SECRET = f"{os.environ.get('API_SECRET')}"
ACCESS_TOKEN = f"{os.environ.get('ACCESS_TOKEN')}"
ACCESS_TOKEN_SECRET = f"{os.environ.get('ACCESS_TOKEN_SECRET')}"

# AUTHORIZATION
auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
# comment
try:
    tweet_text = getClosingPrice()    
    # MAKE TWEET
    api.update_status(tweet_text)
    print("Tweet sent")
except Exception as ex:
    print(f'Could not execute due to: {ex}')
