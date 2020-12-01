from datetime import datetime, timedelta
import decimal
import pandas as pd
import random
import config
import crud_ops
import db_utils
import save_db_locally
import utils

def generate_random_date(start, end):
    """Generate a random datetime between `start` and `end` (inclusive of both)"""
    random_delta_seconds = random.randint(0, int((end - start).total_seconds()))
    return start + timedelta(seconds=random_delta_seconds)

def generate_random_timestamp():
    """Generates random timestamp (between the start of 21st century and current day)"""
    random_dt = generate_random_date(start=datetime(year=2000, month=1, day=1),
                                     end=datetime.now())
    random_ts = utils.datetime_to_timestamp(datetime_obj=random_dt)
    return random_ts

def generate_random_float(start, end):
    """Generates random floating number between `start` and `end` (inclusive of both)"""
    number = decimal.Decimal(str(random.uniform(start, end)))
    number = float(number)
    number = round(number, 4)
    return number

def generate_fake_records(how_many):
    """Generates list of fake records"""
    records = []
    for _ in range(how_many):
        ts = generate_random_timestamp()
        dt = utils.timestamp_to_datetime(timestamp_obj=ts)
        record = {
            '_id': utils.generate_random_id(),
            'reading': generate_random_float(start=10, end=40),
            'timestamp': ts,
            'datetime': str(dt),
            'sensorType': 'temperature'
        }
        records.append(record)
    return records

def reorder_fake_records_by_datetime(records):
    """Re-orders list of fake records in ascending order of date"""
    df_records = pd.DataFrame(data=records)
    df_records.sort_values(by='datetime', ascending=True, ignore_index=True, inplace=True)
    return df_records.to_dict(orient='records')

def add_fake_sensor_records_to_mongodb(how_many):
    records = generate_fake_records(how_many=how_many)
    records = reorder_fake_records_by_datetime(records=records)
    collection = db_utils.get_collection_object(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    collection.insert_many(records)
    return None

if __name__ == "__main__":
    # Adding fake records to the sensor collection in the MongoDB database
    crud_ops.delete_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    add_fake_sensor_records_to_mongodb(how_many=156)
    save_db_locally.save_collection_to_json(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA,
                                            filepath=config.FILEPATH_SENSOR_RECORDS)
    print("Successfully added fake records to the sensor collection in the MongoDB database!")