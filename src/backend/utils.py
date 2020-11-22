import datetime
from datetime import timezone, timedelta
import json
import random

def generate_random_id():
    """Returns random 12 digit ID (str)"""
    random_id = ""
    characters = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for _ in range(12):
        random_id += random.choice(characters)
    return random_id

def save_object_as_json(obj, filepath):
    with open(file=filepath, mode='w') as fp:
        json.dump(obj=obj, fp=fp, indent=4)
    return None

def datetime_to_timestamp(datetime_obj):
    timestamp_obj = datetime_obj.replace(tzinfo=timezone.utc).timestamp()
    timestamp_obj = int(timestamp_obj)
    return timestamp_obj

def timestamp_to_datetime(timestamp_obj):
    datetime_obj = datetime.datetime.fromtimestamp(timestamp_obj)
    datetime_obj = datetime_obj - timedelta(hours=5, minutes=30)
    return datetime_obj

def get_current_timestamp():
    current_dt = datetime.datetime.now()
    current_ts = datetime_to_timestamp(datetime_obj=current_dt)
    return current_ts