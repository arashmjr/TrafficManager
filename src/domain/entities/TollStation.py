from django.db import models
from src.domain.entities.Road import Road


class TollStation(models.Model):
    toll_id = models.BigAutoField(blank=False, primary_key=True)
    road_id = models.ForeignKey(Road, on_delete=models.CASCADE)
    heavy_vehicle_charge = models.IntegerField(blank=False)
    light_vehicle_charge = models.IntegerField(blank=False)
    heavy_vehicle_charge_per_kg = models.IntegerField(blank=False)
    name = models.CharField(max_length=40, blank=False)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=False)

