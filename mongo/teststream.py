# referenced: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Filtered-Stream/filtered_stream.py

import requests
import os
import json
import config
from pymongo import MongoClient

client = MongoClient("mongodb://ishakarki:Boulder92@cluster0-shard-00-00.qwbs1.mongodb.net:27017,cluster0-shard-00-01.qwbs1.mongodb.net:27017,cluster0-shard-00-02.qwbs1.mongodb.net:27017/DaRealDeal?ssl=true&replicaSet=atlas-z12xl7-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["DaRealDeal"]
collection = db["raw_tweets"]

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = config.BEARER_TOKEN_I

def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r

def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line != None or response_line != '':
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
            # mongo tech
            collection.insert_one(json_response)
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