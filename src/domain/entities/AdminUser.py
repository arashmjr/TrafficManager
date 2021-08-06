from django.db import models


class Admin(models.Model):
    admin_id = models.BigAutoField(blank=False, primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=50, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)


