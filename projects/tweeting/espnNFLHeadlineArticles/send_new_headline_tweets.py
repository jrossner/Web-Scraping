import os
import tweepy

def sendNewHeadlineTweets(newHeadlines,api_key,api_secret,access_token,access_token_secret):
    # AUTHORIZATION
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    try:
        for title in newHeadlines.keys():
            tweet_text = f'NEW NFL ARTICLE ON ESPN:\n{newHeadlines[title]["title"]}\n{newHeadlines[title]["link"]}'
            api.update_status(tweet_text)
            print("Tweet sent")
    except Exception as ex:
        print(f'Could not execute "for article in newHeadlines" due to: {ex}')

    print("Finished sending tweets")
