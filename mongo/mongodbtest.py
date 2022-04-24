# referenced: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Filtered-Stream/filtered_stream.py

import requests
import os
import json
import config
from pymongo import MongoClient

client = MongoClient("mongodb+srv://ishakarki:Boulder92@cluster0.qwbs1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["DaRealDeal"]
collection = db["raw_tweets"]

item_1 = {
    "_id" : "U1IT00001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
    "category" : "kitchen appliance"
    }

    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    print(db)
    print(item_1)
    collection.insert_one(item_1)