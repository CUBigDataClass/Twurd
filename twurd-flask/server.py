from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'DaRealDeal'
app.config['MONGO_URI'] = 'mongodb://ishakarki:Boulder92@cluster0-shard-00-00.qwbs1.mongodb.net:27017,cluster0-shard-00-01.qwbs1.mongodb.net:27017,cluster0-shard-00-02.qwbs1.mongodb.net:27017/DaRealDeal?ssl=true&replicaSet=atlas-z12xl7-shard-0&authSource=admin&retryWrites=true&w=majority'

mongo = PyMongo(app)


#https://www.youtube.com/watch?v=7LNl2JlZKHA
@app.route("/frequencies", methods=['GET'])
def get_all_frequencies():
        framework = mongo.db.framework
        output = []

        for q in framework.find():
                output.append({'state': q.state, 'words': [q.words[0], q.words[1], q.words[2]]})
        return jsonify({'result': output})
        
        # return {"state": "Alabama", "words": ["doge", "football", "brother"]}
    
@app.route("/frequencies/<state>", methods=['GET'])
def get_one_frequency(state):
        return {"state": state, "words": ["doge", "football", "brother"]}
    
if __name__ == "__main__":
        app.run(debug=True)