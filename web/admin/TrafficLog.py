from src.domain.entities.TrafficLog import TrafficLog
from django.contrib import admin


class TrafficLogAdmin(admin.ModelAdmin):
    list_display = ['uid', 'plate_number', 'vehicle_type', 'vehicle_color', 'road_width',
                    'date', 'province_name', 'longitude', 'latitude']


admin.site.register(TrafficLog, TrafficLogAdmin)

