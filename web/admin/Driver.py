from src.domain.entities.Driver import Driver
from django.contrib import admin


class DriverAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'name', 'birthdate']


admin.site.register(Driver, DriverAdmin)

