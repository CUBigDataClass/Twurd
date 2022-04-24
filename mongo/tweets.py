import tweepy
import config
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# import pandas as pd

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

class Listener(tweepy.StreamingClient):
    tweets = []
    limit = 10
    
    def on_status(self, status):
        self.tweets.append(status)
        if len(self.tweets) == self.limit:
            self.disconnect()
        print(self.tweets)
    
    def on_tweet(self, tweet):
        print(tweet.data)
        
print("test")
            
streamer = Listener(bearer_token=config.BEARER_TOKEN)
streamer.sample()
# for tweet in range(10):
#     print("test")
#     print(streamer.tweets[tweet])