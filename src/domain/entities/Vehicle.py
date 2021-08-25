from django.db import models
from src.domain.entities.Driver import Driver


class Vehicle(models.Model):
    vehicle_id = models.BigIntegerField(blank=False, primary_key=True)
    national_code = models.ForeignKey(Driver, on_delete=models.CASCADE)
    color = models.CharField(blank=True, max_length=30, null=True)
    type = models.CharField(blank=True, max_length=30, null=True)
    weight = models.BigIntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=30, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)


