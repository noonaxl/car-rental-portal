from decimal import Decimal

from django.db import transaction

from .models import Booking


def calculate_booking_price(booking: Booking) -> Decimal:
    """
    Calculate total booking price based on
    the car daily price and booking duration.
    """

    days = (booking.end_date - booking.start_date).days

    return booking.car.price_per_day * days


@transaction.atomic
def create_booking(
        *,
        user,
        car,
        start_date,
        end_date,
        status="pending",
) -> Booking:
    """
    Create a booking and calculate its total price.
    """

    days = (end_date - start_date).days
    total_price = car.price_per_day * days

    return Booking.objects.create(
        user=user,
        car=car,
        start_date=start_date,
        end_date=end_date,
        status=status,
        total_price=total_price,
    )


@transaction.atomic
def update_booking(
        booking: Booking,
        *,
        user=None,
        car=None,
        start_date=None,
        end_date=None,
        status=None,
) -> Booking:
    """
    Update booking data.

    If the car or booking dates change,
    total_price is recalculated.
    """

    price_changed = False

    if user is not None:
        booking.user = user

    if car is not None:
        booking.car = car
        price_changed = True

    if start_date is not None:
        booking.start_date = start_date
        price_changed = True

    if end_date is not None:
        booking.end_date = end_date
        price_changed = True

    if status is not None:
        booking.status = status

    if price_changed:
        booking.total_price = calculate_booking_price(booking)

    booking.save()

    return booking
