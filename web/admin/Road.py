from src.domain.entities.Road import Road
from django.contrib import admin


class RoadAdmin(admin.ModelAdmin):
    list_display = ['road_id', 'name', 'origin', 'destination', 'minimum_height', 'width']


admin.site.register(Road, RoadAdmin)

