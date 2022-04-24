

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

client = MongoClient("mongodb://ishakarki:Boulder92@cluster0-shard-00-00.qwbs1.mongodb.net:27017,cluster0-shard-00-01.qwbs1.mongodb.net:27017,cluster0-shard-00-02.qwbs1.mongodb.net:27017/DaRealDeal?ssl=true&replicaSet=atlas-z12xl7-shard-0&authSource=admin&retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client["DaRealDeal"]
# collection = db["us_tweets"]

bearer_token = config.BEARER_TOKEN

states = [ '.AK', '.AL', '.AR', '.AZ', '.CA', '.CO', '.CT', '.DC', '.DE', '.FL', '.GA',
           '.HI', '.IA', '.ID', '.IL', '.IN', '.KS', '.KY', '.LA', '.MA', '.MD', '.ME',
           '.MI', '.MN', '.MO', '.MS', '.MT', '.NC', '.ND', '.NE', '.NH', '.NJ', '.NM',
           '.NV', '.NY', '.OH', '.OK', '.OR', '.PA', '.RI', '.SC', '.SD', '.TN', '.TX',
           '.UT', '.VA', '.VT', '.WA', '.WI', '.WV', '.WY']

state = [ '.AK' ]

for name in state:
    megastring = ""
    for doc in db.us_tweets.find({"includes.places.0.full_name": { "$regex": name}}):
        temp = cleaner.clean(doc["data"]["text"])
        megastring += temp
    print(megastring)
    


