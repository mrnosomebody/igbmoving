from django import forms
from phonenumber_field.formfields import PhoneNumberField

from base.enums import ApartmentType


class ApplicationForm(forms.Form):
    YES_NO = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    name = forms.CharField(max_length=85, label='Full Name')
    email = forms.EmailField(max_length=255, label='Email')
    phone = PhoneNumberField(region='CA', label='Mobile Number')  # Get the phone as a string: client.phone.as_e164
    date = forms.DateTimeField(
        label='Moving DateTime',
    )

    address_from = forms.CharField(max_length=255, label='Start address')
    city_from = forms.CharField(label='City')
    zip_from = forms.CharField(label='Zip Code')
    floor_from = forms.IntegerField(label='Floor at PickUp')

    address_to = forms.CharField(max_length=255, label='End address')
    city_to = forms.CharField(label='City')
    zip_to = forms.CharField(label='Zip Code')
    floor_to = forms.IntegerField(label='Floor at DropOff')

    elevator_pickup = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label='Elevator at PickUp')
    elevator_dropoff = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label='Elevator at DropOff')

    promocode = forms.CharField(max_length=255, label='Promocode', required=False)


class MovingForm(ApplicationForm):
    apart_type = forms.ChoiceField(choices=ApartmentType.choices, label='Apartment Type')


class DeliveryForm(ApplicationForm):
    COUNT = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9)
    ]

    large_items = forms.ChoiceField(choices=COUNT, label='Large Items')
    medium_items = forms.ChoiceField(choices=COUNT, label='Medium Items')
