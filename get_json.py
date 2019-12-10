import json
from pymongo import MongoClient
from bson import ObjectId, json_util

if __name__ == '__main__':
    Client = MongoClient()
    db = Client.pts
    cursor = db.members.find({})
    file = open('exported_json.json','w')
    for docu in cursor:
        serial = json.loads(json_util.dumps(cursor))
        file.write(json.dumps(serial))

def getJson(db_name,collection_name):
    Client = MongoClient()
    db = Client.db_name
    cursor = db.collection_name.find({})
    file = open('exported_json.json','w')
    for docu in cursor:
        serial = json.loads(json_util.dumps(cursor))
        file.write(json.dumps(serial))