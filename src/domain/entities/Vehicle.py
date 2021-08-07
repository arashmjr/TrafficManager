from django.db import models
from src.domain.entities.Driver import Driver


class Vehicle(models.Model):
    vehicle_id = models.BigAutoField(blank=False, primary_key=True)
    owner_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    color = models.CharField(blank=True, max_length=30)
    type = models.CharField(blank=False, max_length=30)
    weight = models.BigIntegerField(blank=False)
    height = models.IntegerField(blank=False)
    model = models.CharField(max_length=30, blank=False)
    year = models.IntegerField(blank=False)


