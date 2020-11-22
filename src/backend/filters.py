from typing import List, Optional, Union
import pandas as pd
import config
import crud_ops

def filter_sensor_records(sensor_type: Optional[str] = None,
                          min_reading: Optional[float] = None,
                          max_reading: Optional[float] = None,
                          start_date: Optional[str] = None,
                          end_date: Optional[str] = None) -> Union[List[dict], List]:
    """
    Filters sensor records based on certain parameters.
    >>> filter_sensor_records(sensor_type="temperature",
                              min_reading=16.97,
                              max_reading=25.63,
                              start_date="15-03-2011",
                              end_date="20-11-2020")
    """
    date_format = "%d-%m-%Y"
    records = crud_ops.get_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    df_records = pd.DataFrame(data=records)
    df_records['datetime'] = pd.to_datetime(arg=df_records['datetime'])
    if sensor_type:
        df_records = df_records[df_records['sensorType'].str.lower() == sensor_type.lower().strip()]
    if min_reading:
        df_records = df_records[df_records['reading'] >= min_reading]
    if max_reading:
        df_records = df_records[df_records['reading'] <= max_reading]
    if start_date:
        df_records = df_records[df_records['datetime'] >= pd.to_datetime(arg=start_date, format=date_format)]
    if end_date:
        df_records = df_records[df_records['datetime'] <= pd.to_datetime(arg=end_date, format=date_format)]
    df_records['datetime'] = df_records['datetime'].astype(str)
    return df_records.to_dict(orient='records')