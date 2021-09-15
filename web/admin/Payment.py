from src.domain.entities.Payment import Payment
from django.contrib import admin


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'plate_number', 'toll_id', 'value', 'date', 'status']


admin.site.register(Payment, PaymentAdmin)

