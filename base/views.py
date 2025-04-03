import smtplib
import logging
from django.shortcuts import render, redirect
from django.contrib import messages

from services.orders import create_new_order
from .dto import OrderDTO
from .enums import OrderType
from .forms import MovingForm, DeliveryForm
from services.send_application_by_email import send_email
from captcha_config import SITE_KEY
from services.captcha_is_valid import check_captcha

logger = logging.getLogger(__name__)

def main(request):
    logger.info("Rendering main page")
    return render(request, 'main.html')


def moving(request):
    form = MovingForm()

    if request.method == 'POST':
        logger.info("Received POST request on /moving/")
        form = MovingForm(request.POST)
        logger.debug("Form data: %s", request.POST)
        if form.is_valid():
            logger.info("Form is valid")
            data = form.cleaned_data
            captcha_is_valid = check_captcha(request)
            if captcha_is_valid:
                try:
                    order_dto = OrderDTO(
                        name=data['name'],
                        email=data['email'],
                        phone=data['phone'],
                        date=data['date'],
                        address_from=data['address_from'],
                        city_from=data['city_from'],
                        zip_from=data['zip_from'],
                        address_to=data['address_to'],
                        city_to=data['city_to'],
                        zip_to=data['zip_to'],
                        floor_from=data['floor_from'],
                        floor_to=data['floor_to'],
                        elevator_pickup=data['elevator_pickup'],
                        elevator_dropoff=data['elevator_dropoff'],
                        promocode=data.get('promocode'),
                        apartment_type=data.get('apart_type'),
                        order_type=OrderType.MOVING
                    )
                    order = create_new_order(order_dto)
                    logger.info("Order saved successfully", str(order))
                    messages.success(request, "Success")
                    try:
                        send_email(data, 'Moving')
                    except Exception as e:
                        logger.error("Error while sending email: %s", e, exc_info=True)
                        messages.error(request, "Server error occurred, we didn't get your application")
                        return redirect('moving')
                    return redirect('moving')

                except smtplib.SMTPException as e:
                    logger.error("SMTP error while sending email: %s", e, exc_info=True)
                    messages.error(request, "Server error occurred, we didn't get your application")

                except Exception as e:
                    logger.error("Unexpected error: %s", e, exc_info=True)
                    messages.error(request, "Unexpected error occurred. Please try again later.")
            else:
                logger.warning("Captcha invalid")
                messages.error(request, "Invalid Captcha, try again, please")
        else:
            logger.warning("Form errors: %s", form.errors)
            messages.error(request, "Error")
    else:
        logger.debug("GET request on /moving/")

    return render(request, 'moving.html', {'form': form, 'captcha_key': SITE_KEY})


def delivery(request):
    form = DeliveryForm()

    if request.method == 'POST':
        logger.info("Received POST request on /delivery/")
        form = DeliveryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            captcha_is_valid = check_captcha(request)
            if captcha_is_valid:
                try:
                    order_dto = OrderDTO(
                        name=data['name'],
                        email=data['email'],
                        phone=data['phone'],
                        date=data['date'],
                        address_from=data['address_from'],
                        city_from=data['city_from'],
                        zip_from=data['zip_from'],
                        address_to=data['address_to'],
                        city_to=data['city_to'],
                        zip_to=data['zip_to'],
                        floor_from=data['floor_from'],
                        floor_to=data['floor_to'],
                        elevator_pickup=data['elevator_pickup'],
                        elevator_dropoff=data['elevator_dropoff'],
                        promocode=data.get('promocode'),
                        large_items=data.get('large_items'),
                        medium_items=data.get('medium_items'),
                        order_type=OrderType.DELIVERY
                    )
                    order = create_new_order(order_dto)
                    logger.info("Order saved successfully", str(order))
                    messages.success(request, "Success")
                    try:
                        send_email(data, 'Delivery')
                    except Exception as e:
                        logger.error("Error while sending email: %s", e, exc_info=True)
                        messages.error(request, "Server error occurred, we didn't get your application")
                        return redirect('delivery')

                    return redirect('delivery')

                except smtplib.SMTPException as e:
                    logger.error("SMTP error while sending email for Delivery: %s", e, exc_info=True)
                    messages.error(request, f"{e} (Server error occurred, we didn't get your application)")

                except Exception as e:
                    logger.error("Unexpected error in Delivery view: %s", e, exc_info=True)
                    messages.error(request, f"{e} Unexpected error occurred. Please try again later.")
            else:
                logger.warning("Invalid captcha in Delivery view")
                messages.error(request, "Invalid Captcha, try again, please")
        else:
            logger.warning("Form errors in Delivery view: %s", form.errors)
            messages.error(request, "Error")
    else:
        logger.debug("GET request on /delivery/")

    return render(request, 'delivery.html', {'form': form, 'captcha_key': SITE_KEY})


def terms_and_conditions(request):
    logger.info("Rendering terms and conditions page")
    return render(request, 'terms_and_conditions.html')
