from django.db import models


class Road(models.Model):
    road_id = models.BigAutoField(blank=False, primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    origin = models.CharField(blank=False, max_length=40)
    destination = models.CharField(blank=False, max_length=40)
    minimum_height = models.FloatField(blank=False)
    width = models.FloatField(blank=False)


