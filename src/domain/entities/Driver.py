from django.db import models


class Driver(models.Model):
    national_code = models.BigIntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    birthdate = models.IntegerField(blank=True, null=True)

