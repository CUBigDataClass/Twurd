from flask import Flask, jsonify, request
from flask_pymongo import  MongoClient
from dotenv import load_dotenv
import pprint
import os


app = Flask(__name__)

def main(): 
        load_dotenv()
        client = MongoClient(os.getenv('MONGO_CLIENT'), tls=True, tlsAllowInvalidCertificates=True)
        db = client["DaRealDeal"]
        collection = db["us_tweets"]
        for doc in collection.find():
         pprint.pprint(doc)

#https://www.youtube.com/watch?v=7LNl2JlZKHA
@app.route("/frequencies", methods=['GET'])
def get_all_frequencies():
        return {"state": "Alabama", "words": ["doge", "football", "brother"]}
    
@app.route("/frequencies/<state>", methods=['GET'])
def get_one_frequency(state):
        return {"state": state, "words": ["doge", "football", "brother", "Calista", "Vananh", "John", "Amey", "David", "Isha"], "freq": [1, 0.8, 0.2, 0.5, 0.6, 0.1, 0.3, 0.7, 0.4 ]}
    
if __name__ == "__main__":
        main()
        app.run(debug=True)