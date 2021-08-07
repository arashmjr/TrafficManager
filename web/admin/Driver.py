from src.domain.entities.Driver import Driver
from django.contrib import admin


class DriverAdmin(admin.ModelAdmin):
    list_display = ['driver_id', 'name', 'birthdate', 'national_code']


admin.site.register(Driver, DriverAdmin)

