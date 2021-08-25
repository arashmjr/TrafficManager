from django.contrib.gis.db.models import LineStringField
from django.db import models


class Road(models.Model):
    road_id = models.BigAutoField(blank=False, primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    geom = LineStringField(srid=4326)
    minimum_height = models.FloatField(blank=False)
    width = models.FloatField(blank=False)


