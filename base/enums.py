from django.db import models

class ApartmentType(models.TextChoices):
    STUDIO = 'Studio', 'Studio'
    ONE_BEDROOM = '1 Bedroom', '1 Bedroom'
    TWO_BEDROOM = '2 Bedroom', '2 Bedroom'
    THREE_BEDROOM = '3 Bedroom', '3 Bedroom'
    FOUR_BEDROOM = '4 Bedroom', '4 Bedroom'
    MULTILEVEL_CONDO_UP_TO_750 = 'Multilevel Condo - Up to 750 sqft', 'Multilevel Condo - Up to 750 sqft'
    MULTILEVEL_CONDO_UP_TO_1000 = 'Multilevel Condo - Up to 1000 sqft', 'Multilevel Condo - Up to 1000 sqft'
    MULTILEVEL_CONDO_UP_TO_1250 = 'Multilevel Condo - Up to 1250 sqft', 'Multilevel Condo - Up to 1250 sqft'
    MULTILEVEL_CONDO_UP_TO_1500 = 'Multilevel Condo - Up to 1500 sqft', 'Multilevel Condo - Up to 1500 sqft'
    MULTILEVEL_CONDO_UP_TO_2000 = 'Multilevel Condo - Up to 2000 sqft', 'Multilevel Condo - Up to 2000 sqft'
    HOUSE_UP_TO_1000 = 'House - Up to 1000 sqft', 'House - Up to 1000 sqft'
    HOUSE_UP_TO_1500 = 'House - Up to 1500 sqft', 'House - Up to 1500 sqft'
    HOUSE_UP_TO_2000 = 'House - Up to 2000 sqft', 'House - Up to 2000 sqft'
    HOUSE_UP_TO_2500 = 'House - Up to 2500 sqft', 'House - Up to 2500 sqft'
    HOUSE_UP_TO_3000 = 'House - Up to 3000 sqft', 'House - Up to 3000 sqft'
    OFFICE_UP_TO_750 = 'Office - Up to 750 sqft', 'Office - Up to 750 sqft'
    OFFICE_UP_TO_1000 = 'Office - Up to 1000 sqft', 'Office - Up to 1000 sqft'
    OFFICE_UP_TO_1500 = 'Office - Up to 1500 sqft', 'Office - Up to 1500 sqft'
    OFFICE_UP_TO_2000 = 'Office - Up to 2000 sqft', 'Office - Up to 2000 sqft'
    OFFICE_UP_TO_2500 = 'Office - Up to 2500 sqft', 'Office - Up to 2500 sqft'
    OFFICE_UP_TO_3000 = 'Office - Up to 3000 sqft', 'Office - Up to 3000 sqft'


class OrderStatus(models.TextChoices):
    NEW = 'New', 'New'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'
    CANCELED = 'Canceled', 'Canceled'

class OrderType(models.TextChoices):
    MOVING = 'Moving', 'Moving'
    DELIVERY = 'Delivery', 'Delivery'