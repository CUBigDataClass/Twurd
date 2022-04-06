import tweepy
import config
# import pandas as pd

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth)

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
for tweet in streamer.tweets:
    print("test")
    print(tweet)