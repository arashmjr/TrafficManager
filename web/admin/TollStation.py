from src.domain.entities.TollStation import TollStation
from django.contrib import admin


class TollStationAdmin(admin.ModelAdmin):
    list_display = ['toll_id', 'road_id', 'heavy_vehicle_charge', 'light_vehicle_charge', 'heavy_vehicle_charge_per_kg',
                    'name', 'latitude', 'longitude']


admin.site.register(TollStation, TollStationAdmin)
