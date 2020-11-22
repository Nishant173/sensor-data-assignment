import pandas as pd
import config
import crud_ops
import utils

def get_sensor_statistics(start_date, end_date):
    """
    Gets min/max/median/average stats of the 'reading' for all sensor records available between
    certain date-range. The format of dates must be string of 'dd-mm-yyyy'.
    Eg: get_sensor_statistics(start_date="14-06-2000", end_date="31-12-2005")
    Returns dictionary of stats. Returns empty dictionary if no sensor data is available for given date-range.
    """
    date_format = "%d-%m-%Y"
    records = crud_ops.get_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    df_records = pd.DataFrame(data=records)
    df_records['datetime'] = df_records['timestamp'].apply(utils.timestamp_to_datetime)
    is_after_start_date = df_records['datetime'] >= pd.to_datetime(arg=start_date, format=date_format)
    is_before_end_date = df_records['datetime'] <= pd.to_datetime(arg=end_date, format=date_format)
    df_records = df_records[is_after_start_date & is_before_end_date]
    if df_records.empty:
        return {}
    dictionary_stats = {
        'min': df_records['reading'].min(),
        'max': df_records['reading'].max(),
        'median': df_records['reading'].median(),
        'average': df_records['reading'].mean(),
        'startDate': start_date,
        'endDate': end_date,
        'numberOfRecords': int(len(df_records)),
    }
    return dictionary_stats