

from telnetlib import TLS
import requests
import json
import tweepy
import config
from pymongo import MongoClient
import cleaner

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth)

db = client["DaRealDeal"]
collection = db["states"]

bearer_token = config.BEARER_TOKEN

states = [ '.AK', '.AL', '.AR', '.AZ', '.CA', '.CO', '.CT', '.DE', '.FL', '.GA',
           '.HI', '.IA', '.ID', '.IL', '.IN', '.KS', '.KY', '.LA', '.MA', '.MD', '.ME',
           '.MI', '.MN', '.MO', '.MS', '.MT', '.NC', '.ND', '.NE', '.NH', '.NJ', '.NM',
           '.NV', '.NY', '.OH', '.OK', '.OR', '.PA', '.RI', '.SC', '.SD', '.TN', '.TX',
           '.UT', '.VA', '.VT', '.WA', '.WI', '.WV', '.WY']

state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", 
                "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", 
                "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", 
                "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", 
                "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", 
                "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
                "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

for i in range(len(states)):
    megastring = ""
    for doc in db.us_tweets.find({"includes.places.0.full_name": { "$regex": states[i]}}):
        temp = cleaner.clean(doc["data"]["text"])
        megastring += temp
    megastring = " ".join(megastring.split())
    post = {"state":state_names[i], "combined_text": megastring}
    print(states[i])
    print(post)
    # collection.insert_one(post)
    


