from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ApplicationForm(forms.Form):
    YES_NO = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    name = forms.CharField(max_length=85, label='Full Name')
    email = forms.EmailField(max_length=255, label='Email')
    phone = PhoneNumberField(region='CA', label='Mobile Number')  # Get the phone as a string: client.phone.as_e164
    date = forms.DateField(label='Date')

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
    TYPE_AND_SIZE_OF_DWELLING = [
        ('Studio', 'Studio'),
        ('1 Bedroom', '1 Bedroom'),
        ('2 Bedroom', '2 Bedroom'),
        ('3 Bedroom', '3 Bedroom'),
        ('4 Bedroom', '4 Bedroom'),
        ('Multilevel Condo - Up to 750 sqft', 'Multilevel Condo - Up to 750 sqft'),
        ('Multilevel Condo - Up to 1000 sqft', 'Multilevel Condo - Up to 1000 sqft'),
        ('Multilevel Condo - Up to 1250 sqft', 'Multilevel Condo - Up to 1250 sqft'),
        ('Multilevel Condo - Up to 1500 sqft', 'Multilevel Condo - Up to 1500 sqft'),
        ('Multilevel Condo - Up to 2000 sqft', 'Multilevel Condo - Up to 2000 sqft'),
        ('House - Up to 1000 sqft', 'House - Up to 1000 sqft'),
        ('House - Up to 1500 sqft', 'House - Up to 1500 sqft'),
        ('House - Up to 2000 sqft', 'House - Up to 2000 sqft'),
        ('House - Up to 2500 sqft', 'House - Up to 2500 sqft'),
        ('House - Up to 3000 sqft', 'House - Up to 3000 sqft'),
        ('Office - Up to 750 sqft', 'Office - Up to 750 sqft'),
        ('Office - Up to 1000 sqft', 'Office - Up to 1000 sqft'),
        ('Office - Up to 1500 sqft', 'Office - Up to 1500 sqft'),
        ('Office - Up to 2000 sqft', 'Office - Up to 2000 sqft'),
        ('Office - Up to 2500 sqft', 'Office - Up to 2500 sqft'),
        ('Office - Up to 3000 sqft', 'Office - Up to 3000 sqft')
    ]

    apart_type = forms.ChoiceField(choices=TYPE_AND_SIZE_OF_DWELLING, label='Type&Size of Dwelling')


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
