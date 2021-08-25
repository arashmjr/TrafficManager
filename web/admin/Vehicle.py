from src.domain.entities.Vehicle import Vehicle
from django.contrib import admin


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_id', 'national_code', 'color', 'type', 'weight', 'height', 'model', 'year']


admin.site.register(Vehicle, VehicleAdmin)
