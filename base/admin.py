from django.contrib import admin
from django.utils.html import format_html
from .models import Order, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'zip_code', 'floor', 'has_elevator')
    search_fields = ('address', 'city')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'moving_date', 'submission_date', 'order_type', 'status')
    readonly_fields = ('submission_date', 'start_address_info', 'end_address_info',)

    def start_address_info(self, obj):
        addr = obj.start_address
        if addr:
            return format_html(
                "Address: {}<br>City: {}<br>Floor: {}<br>Zip: {}<br>Elevator: {}",
                addr.address,
                addr.city,
                addr.floor,
                addr.zip_code,
                "Yes" if addr.has_elevator else "No"
            )
        return "-"
    start_address_info.short_description = "Start Address"

    def end_address_info(self, obj):
        addr = obj.end_address
        if addr:
            return format_html(
                "Address: {}<br>City: {}<br>Floor: {}<br>Zip: {}<br>Elevator: {}",
                addr.address,
                addr.city,
                addr.floor,
                addr.zip_code,
                "Yes" if addr.has_elevator else "No"
            )
        return "-"
    end_address_info.short_description = "End Address"
