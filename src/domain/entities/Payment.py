from django.db import models
from src.domain.entities.Vehicle import Vehicle
from src.domain.entities.TollStation import TollStation
from spatialapp.domain.entities.Road import Road


class Payment(models.Model):
    payment_id = models.BigAutoField(blank=False, primary_key=True)
    plate_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    toll_id = models.ForeignKey(TollStation, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=30)

