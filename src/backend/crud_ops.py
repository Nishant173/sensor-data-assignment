from typing import List
import pandas as pd
import config
import db_utils
import utils

def get_all_records_from_mongodb(collection_name) -> List:
    """Returns list of all records in a collection from the MongoDB database"""
    collection = db_utils.get_collection_object(collection_name=collection_name)
    all_posts = list(collection.find({}))
    return all_posts

def delete_all_records_from_mongodb(collection_name) -> None:
    """Deletes all records from a collection in the MongoDB database"""
    collection = db_utils.get_collection_object(collection_name=collection_name)
    collection.delete_many({})
    return None

def get_sensor_record(record_id: str) -> dict:
    """Gets one record from the sensor collection (based on '_id') in the MongoDB database"""
    records = get_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    df_records = pd.DataFrame(data=records)
    df_record = df_records[df_records['_id'] == record_id]
    if df_record.empty:
        return {}
    if len(df_record) == 1:
        record_obj = df_record.iloc[0].to_dict()
        record_obj['reading'] = float(record_obj['reading'])
        record_obj['timestamp'] = int(record_obj['timestamp'])
        return record_obj
    raise Exception("Multiple records with same ID exists")

def add_sensor_record(reading: float, sensor_type: str) -> None:
    """Adds one record to the sensor collection in the MongoDB database"""
    collection = db_utils.get_collection_object(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    ts = utils.get_current_timestamp()
    dt = utils.timestamp_to_datetime(timestamp_obj=ts)
    obj_to_add = {
        '_id': utils.generate_random_id(),
        'reading': reading,
        'timestamp': ts,
        'datetime': str(dt),
        'sensorType': sensor_type,
    }
    collection.insert_one(obj_to_add)
    return None

def delete_sensor_record(record_id: str) -> None:
    """Deletes one record from the sensor collection (based on '_id') in the MongoDB database"""
    collection = db_utils.get_collection_object(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    collection.delete_one({"_id": record_id})
    return None