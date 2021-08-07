from src.domain.entities.Payment import Payment
from django.contrib import admin


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'vehicle_id', 'toll_id', 'road_id', 'value', 'date', 'status']


admin.site.register(Payment, PaymentAdmin)

