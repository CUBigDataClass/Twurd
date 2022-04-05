from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://ishakarki:Boulder92@cluster0-shard-00-00.qwbs1.mongodb.net:27017,cluster0-shard-00-01.qwbs1.mongodb.net:27017,cluster0-shard-00-02.qwbs1.mongodb.net:27017/twurd?ssl=true&replicaSet=atlas-z12xl7-shard-0&authSource=admin&retryWrites=true&w=majority", connect=False)
db=client.test
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)