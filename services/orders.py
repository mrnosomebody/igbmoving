from urllib.response import addbase

from base.dto import OrderDTO
from django.db import transaction

from base.models import Order, Address


@transaction.atomic
def save_new_order(order_dto: OrderDTO) -> Order:
    address_from = Address.objects.create(
        address=order_dto.address_from,
        city=order_dto.city_from,
        floor=order_dto.floor_from,
        zip_code=order_dto.zip_from,
        has_elevator=order_dto.elevator_pickup == 'Yes',
    )
    address_to = Address.objects.create(
        address=order_dto.address_to,
        city=order_dto.city_to,
        floor=order_dto.floor_to,
        zip_code=order_dto.zip_to,
        has_elevator=order_dto.elevator_pickup == 'Yes',
    )

    order = Order.objects.create(
        full_name=order_dto.name,
        email=order_dto.email,
        phone=order_dto.phone,
        moving_date=order_dto.date,
        start_address=address_from,
        end_address=address_to,
        apartment_type=order_dto.apartment_type,
        promocode=order_dto.promocode,
    )

    return order