import os
from get_espn_nfl_headlines import getEspnNFLHeadlines
from check_for_new_headlines import checkIfNewHeadlines
from store_last_headline import storeLastHeadline
from send_new_headline_tweets import sendNewHeadlineTweets

# SECRETS
API_KEY = f"{os.environ.get('API_KEY')}"
API_SECRET = f"{os.environ.get('API_SECRET')}"
ACCESS_TOKEN = f"{os.environ.get('ACCESS_TOKEN')}"
ACCESS_TOKEN_SECRET = f"{os.environ.get('ACCESS_TOKEN_SECRET')}"

try:
  last_headline = json.load(open('last_headline.json'))
except:
  last_headline = {}
  
try:
  current_headlines = getEspnNFLHeadlines()
  new_headlines = checkIfNewHeadlines(current_headlines,last_headline)
  storeLastHeadline(new_headlines)
  sendNewHeadlineTweets(new_headlines,API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
  print("Script completed")
except Exception as ex:
  print(f'Could not complete this script due to: {ex}')
