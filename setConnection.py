#setConnection.py
import config, pymongo

def call():
    myclient = pymongo.MongoClient(config.kdict['MONGODB_URI'])
    mongodb = myclient["multimedia"]
    mongocol = mongodb["users"]

    return mongocol