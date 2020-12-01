from rest_framework.decorators import api_view
from rest_framework.response import Response
from .business_logic import config, crud_ops, filters, stat_calc

@api_view(['GET'])
def api_home(request):
    return Response(data="This is the API Home page. Please visit '<www.domain.com>/api/documentation' for details")


@api_view(['GET'])
def documentation(request):
    endpoints = [
        {
            'endpoint': '/api/sensor/records',
            'description': 'Gets all sensor records',
            'parameters': [],
            'example': '/api/sensor/records',
            'methods': ['GET'],
        },
        {
            'endpoint': '/api/sensor/records/<str:_id>',
            'description': 'Gets one sensor record by ID',
            'parameters': [],
            'example': '/api/sensor/records/IPKR8IF8BCVZ',
            'methods': ['GET'],
        },
        {
            'endpoint': '/api/sensor/records/filter',
            'description': 'Filters sensor records (based on certain parameters)',
            'parameters': [
                {
                    'name': 'sensorType',
                    'datatype': 'str',
                    'required': False,
                },
                {
                    'name': 'minReading',
                    'datatype': 'float',
                    'required': False,
                },
                {
                    'name': 'maxReading',
                    'datatype': 'float',
                    'required': False,
                },
                {
                    'name': 'startDate',
                    'datatype': 'str',
                    'format': 'dd-mm-yyyy',
                    'required': False,
                },
                {
                    'name': 'endDate',
                    'datatype': 'str',
                    'format': 'dd-mm-yyyy',
                    'required': False,
                },
            ],
            'example': '/api/sensor/records/filter?sensorType=temperature&minReading=10.223&maxReading=14.472&startDate=14-06-2020&endDate=31-12-2020',
            'methods': ['GET'],
        },
        {
            'endpoint': '/api/sensor/records/stats',
            'description': 'Gets sensor related statistics (based on certain parameters)',
            'parameters': [
                {
                    'name': 'startDate',
                    'datatype': 'str',
                    'format': 'dd-mm-yyyy',
                    'required': True,
                },
                {
                    'name': 'endDate',
                    'datatype': 'str',
                    'format': 'dd-mm-yyyy',
                    'required': True,
                },
            ],
            'example': '/api/sensor/records/stats?startDate=14-06-2020&endDate=31-12-2020',
            'methods': ['GET'],
        },
        {
            'endpoint': '/api/sensor/records/add',
            'description': 'Adds one sensor record (based on certain parameters)',
            'parameters': [
                {
                    'name': 'reading',
                    'datatype': 'float',
                    'required': True,
                },
                {
                    'name': 'sensorType',
                    'datatype': 'str',
                    'required': True,
                },
            ],
            'example': '/api/sensor/records/add?reading=10.224&sensorType=temperature',
            'methods': ['POST'],
        },
        {
            'endpoint': '/api/sensor/records/delete/<str:_id>',
            'description': 'Deletes one sensor record by ID',
            'parameters': [],
            'example': '/api/sensor/records/delete/IPKR8IF8BCVZ',
            'methods': ['DELETE'],
        },
    ]
    return Response(data=endpoints)


@api_view(['GET'])
def all_sensor_records(request):
    records = crud_ops.get_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    return Response(data=records)


@api_view(['GET'])
def get_sensor_record(request, _id):
    record_id = str(_id)
    record = crud_ops.get_sensor_record(record_id=record_id)
    return Response(data=record)


@api_view(['GET'])
def filter_sensor_records(request):
    sensor_type = request.GET.get('sensorType', default=None)
    min_reading = request.GET.get('minReading', default=None)
    max_reading = request.GET.get('maxReading', default=None)
    start_date = request.GET.get('startDate', default=None)
    end_date = request.GET.get('endDate', default=None)
    records = crud_ops.get_all_records_from_mongodb(collection_name=config.MONGODB_COLLECTION_SENSOR_DATA)
    records = filters.filter_sensor_records(records=records,
                                            sensor_type=sensor_type,
                                            min_reading=float(min_reading) if min_reading else None,
                                            max_reading=float(max_reading) if max_reading else None,
                                            start_date=start_date,
                                            end_date=end_date)
    return Response(data=records)


@api_view(['GET'])
def sensor_stats(request):
    start_date = request.GET['startDate']
    end_date = request.GET['endDate']
    dictionary_stats = stat_calc.get_sensor_statistics(start_date=start_date,
                                                       end_date=end_date)
    return Response(data=dictionary_stats)


@api_view(['GET', 'POST'])
def add_sensor_record(request):
    reading = float(request.GET['reading'])
    sensor_type = str(request.GET['sensorType'])
    crud_ops.add_sensor_record(reading=reading,
                               sensor_type=sensor_type)
    response = {"message": "Record was added successfully", "status_code": 201}
    return Response(data=response)


@api_view(['GET', 'DELETE'])
def delete_sensor_record(request, _id):
    record_id = str(_id)
    crud_ops.delete_sensor_record(record_id=record_id)
    response = {"message": "Record was deleted successfully", "status_code": 200}
    return Response(data=response)