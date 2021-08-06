from django.db import models


class Driver(models.Model):
    driver_id = models.BigAutoField(blank=False, primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    birthdate = models.DateField(blank=True, null=True)
    national_code = models.BigIntegerField(blank=False)
