import datetime

from pydantic import BaseModel
from phonenumber_field.formfields import PhoneNumber

from base.enums import OrderType, OrderStatus


class OrderDTO(BaseModel):
    name: str
    email: str
    phone: PhoneNumber
    date: datetime.datetime
    address_from: str
    city_from: str
    zip_from: str
    address_to: str
    city_to: str
    zip_to: str
    floor_from: int
    floor_to: int
    elevator_pickup: str
    elevator_dropoff: str
    promocode: str = None
    apartment_type: str | None = None
    large_items: int | None = None
    medium_items: int | None = None
    order_type: OrderType
    status: OrderStatus | None = None


    class Config:
        arbitrary_types_allowed = True