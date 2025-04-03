from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from base.enums import ApartmentType, OrderStatus, OrderType


class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    floor = models.IntegerField()
    zip_code = models.CharField(max_length=20)
    has_elevator = models.BooleanField()


class Order(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField(region='CA')
    submission_date = models.DateTimeField(auto_now_add=True, editable=False)
    moving_date = models.DateTimeField()
    start_address = models.ForeignKey('Address', related_name='start_address', on_delete=models.CASCADE)
    end_address = models.ForeignKey('Address', related_name='end_address', on_delete=models.CASCADE)
    promocode = models.CharField(max_length=55, blank=True, null=True)
    status = models.CharField(max_length=255, choices=OrderStatus.choices, default=OrderStatus.NEW)

    order_type = models.CharField(max_length=255, choices=OrderType.choices)
    apartment_type = models.CharField(max_length=255, choices=ApartmentType.choices, null=True, blank=True)
    large_items = models.IntegerField(null=True, blank=True)
    medium_items = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.moving_date.strftime('%Y-%m-%d %H:%M')}"
