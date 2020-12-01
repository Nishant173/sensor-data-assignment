from django.urls import path
from . import views

urlpatterns = [
    path(route='documentation', view=views.documentation, name='documentation'),
    path(route='sensor/records', view=views.all_sensor_records, name='all-sensor-records'),
    path(route='sensor/records/<str:_id>', view=views.get_sensor_record, name='get-sensor-record'),
    path(route='sensor/records/filter', view=views.filter_sensor_records, name='filter-sensor-records'),
    path(route='sensor/records/stats', view=views.sensor_stats, name='sensor-stats'),
    path(route='sensor/records/add', view=views.add_sensor_record, name='add-sensor-record'),
    path(route='sensor/records/delete/<str:_id>', view=views.delete_sensor_record, name='delete-sensor-record'),
]