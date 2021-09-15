from django.db import models
from spatialapp.domain.entities.Road import Road


class TollStation(models.Model):
    toll_id = models.BigAutoField(blank=False, primary_key=True)
    road_id = models.ForeignKey(Road, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40, blank=False)
    heavy_vehicle_charge = models.IntegerField(blank=True, null=True)
    light_vehicle_charge = models.IntegerField(blank=True, null=True)
    heavy_vehicle_charge_per_kg = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)


