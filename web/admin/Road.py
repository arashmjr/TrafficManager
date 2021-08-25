from src.domain.entities.Road import Road
from django.contrib import admin


class RoadAdmin(admin.ModelAdmin):
    list_display = ['road_id', 'name', 'geom', 'minimum_height', 'width']


admin.site.register(Road, RoadAdmin)

