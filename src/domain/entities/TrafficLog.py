from django.db import models
from spatialapp.domain.entities.Road import Road
from src.domain.entities.Vehicle import Vehicle
import datetime


class TrafficLog(models.Model):
    uid = models.BigAutoField(blank=False, primary_key=True)
    plate_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_type = models.CharField(blank=True, max_length=30, null=True)
    vehicle_color = models.CharField(blank=True, max_length=30, null=True)
    road_width = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    province_name = models.CharField(blank=True, max_length=30, null=True)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)

    class Meta:
        app_label = 'src'
