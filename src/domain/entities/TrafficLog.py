from django.db import models
from src.domain.entities.Road import Road
from src.domain.entities.Vehicle import Vehicle
import datetime


class TrafficLog(models.Model):
    uid = models.BigAutoField(blank=False, primary_key=True)
    road_id = models.ForeignKey(Road, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vehicle_type = models.CharField(blank=False, max_length=30)
    vehicle_color = models.CharField(blank=True, max_length=30)
    road_width = models.IntegerField(blank=False)
    date = models.DateTimeField(default=datetime.datetime.now)
    province_name = models.CharField(blank=False, max_length=30)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=False)
