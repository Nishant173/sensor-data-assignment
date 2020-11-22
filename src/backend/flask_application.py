from flask import Flask, jsonify, request
import config
import crud_ops
import filters
import save_db_locally
import stat_calc

app = Flask(__name__)

@app.route(rule='/', methods=['GET'])
def home():
    return "<h1>This is the Home page</h1>"


@app.route(rule='/sensor/records', methods=['GET'])
def all_sensor_records():
    return jsonify(crud_ops.get_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA))


@app.route(rule='/sensor/records/filter', methods=['GET'])
def filter_sensor_records():
    sensor_type = request.args.get('sensorType', default=None)
    min_reading = request.args.get('minReading', default=None)
    max_reading = request.args.get('maxReading', default=None)
    start_date = request.args.get('startDate', default=None)
    end_date = request.args.get('endDate', default=None)
    records = filters.filter_sensor_records(sensor_type=sensor_type,
                                            min_reading=float(min_reading) if min_reading else None,
                                            max_reading=float(max_reading) if max_reading else None,
                                            start_date=start_date,
                                            end_date=end_date)
    return jsonify(records), 200


@app.route(rule='/sensor/stats', methods=['GET'])
def sensor_stats():
    start_date = str(request.args['startDate'])
    end_date = str(request.args['endDate'])
    dictionary_stats = stat_calc.get_sensor_statistics(start_date=start_date, end_date=end_date)
    return jsonify(dictionary_stats), 200


@app.route(rule='/sensor/record', methods=['GET'])
def get_sensor_record():
    record_id = str(request.args['_id'])
    record = crud_ops.get_sensor_record(record_id=record_id)
    return jsonify(record), 200


@app.route(rule='/sensor/record/add', methods=['GET', 'POST'])
def add_sensor_record():
    reading = float(request.args['reading'])
    sensor_type = request.args['sensorType']
    crud_ops.add_sensor_record(reading=reading, sensor_type=sensor_type)
    save_db_locally.save_collection_to_json(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA,
                                            filepath=config.FILEPATH_SENSOR_RECORDS)
    response = {"message": "Record was added successfully", "status_code": 201}
    return jsonify(response), 201


@app.route(rule='/sensor/record/delete', methods=['GET', 'DELETE'])
def delete_sensor_record():
    record_id = str(request.args['_id'])
    crud_ops.delete_sensor_record(record_id=record_id)
    save_db_locally.save_collection_to_json(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA,
                                            filepath=config.FILEPATH_SENSOR_RECORDS)
    response = {"message": "Record was deleted successfully", "status_code": 200}
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)