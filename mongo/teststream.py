# referenced: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Filtered-Stream/filtered_stream.py

from telnetlib import TLS
import requests
import os
import json
import tweepy
import config
from pymongo import MongoClient

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth)

client = MongoClient("mongodb://ishakarki:Boulder92@cluster0-shard-00-00.qwbs1.mongodb.net:27017,cluster0-shard-00-01.qwbs1.mongodb.net:27017,cluster0-shard-00-02.qwbs1.mongodb.net:27017/DaRealDeal?ssl=true&replicaSet=atlas-z12xl7-shard-0&authSource=admin&retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.test
db = client["DaRealDeal"]
collection = db["raw_tweets"]

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = config.BEARER_TOKEN

def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r
#"place_id": "01da545b582fc86b"
def connect_to_endpoint(url, next_token = None):
    query_params = {
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'place.fields': 'full_name,country_code,country',
                    }
    query_params['next_token'] = next_token
    
    response = requests.request("GET", url, auth=bearer_oauth, stream=True, params=query_params)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line != None or response_line != '':
            json_response = json.loads(response_line)
            # id = str(json_response['data']['author_id'])
            # user = api.get_user(user_id=id)
            # location = user.location
            # print(location)
            #print(json_response['data']['author_id'])
            if json_response['data']['geo'] and json_response['includes']['places'][0]['country_code'] == "US":
                print(json.dumps(json_response, indent=4, sort_keys=True))
                collection.insert_one(json_response)
                
            #print(json.dumps(json_response, indent=4, sort_keys=True))
            # mongo tech

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()