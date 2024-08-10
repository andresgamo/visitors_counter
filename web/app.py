from flask import Flask, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)


client = MongoClient("mongodb://mongo:27017")
db = client["visitorsdb"]
counter_collection = db["counter"]

class Visitor(Resource):
    def get(self):
        counter = counter_collection.find_one_and_update(
            {}, 
            {"$inc": {"count": 1}},
            upsert=True,
            return_document=True
        )
        return jsonify({
            "message": f"{counter.get('count')} visitor"
        })
    
api.add_resource(Visitor,"/home")


if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)