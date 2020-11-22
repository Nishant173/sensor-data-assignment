import crud_ops
import utils

def save_collection_to_json(collection_name, filepath):
    """Saves JSON file of current snapshot of a collection from the MongoDB database"""
    records = crud_ops.get_all_records_from_mongodb(collection_name=collection_name)
    utils.save_object_as_json(obj=records, filepath=filepath)
    return None