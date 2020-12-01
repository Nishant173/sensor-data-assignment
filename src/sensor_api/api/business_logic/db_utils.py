from pymongo import MongoClient
from . import config

def get_collection_object(collection_name):
    """Returns object of the collection instance from the MongoDB database"""
    cluster = MongoClient(config.MONGODB_CONNECTION_URI)
    db = cluster[config.MONGODB_DB_NAME]
    collection_obj = db[collection_name]
    return collection_obj