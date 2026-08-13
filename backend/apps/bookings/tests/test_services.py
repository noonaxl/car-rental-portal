from datetime import date
from decimal import Decimal

from django.test import TestCase

from apps.bookings.services import create_booking, update_booking
from apps.cars.models import Car, Category
from apps.users.models import User


class BookingServiceTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )

        self.category = Category.objects.create(
            name="SUV",
            description="Sport utility vehicles",
        )

        self.car = Car.objects.create(
            brand="BMW",
            model="X5",
            year=2024,
            price_per_day=Decimal("100.00"),
            category=self.category,
        )

    def test_create_booking_calculates_total_price(self):
        booking = create_booking(
            user=self.user,
            car=self.car,
            start_date=date(2026, 10, 10),
            end_date=date(2026, 10, 15),
        )

        self.assertEqual(
            booking.total_price,
            Decimal("500.00"),
        )

        self.assertEqual(
            booking.status,
            "pending",
        )

    def test_update_booking_recalculates_price_when_car_changes(self):
        expensive_car = Car.objects.create(
            brand="Mercedes",
            model="C-Class",
            year=2024,
            price_per_day=Decimal("200.00"),
            category=self.category,
        )

        booking = create_booking(
            user=self.user,
            car=self.car,
            start_date=date(2026, 10, 10),
            end_date=date(2026, 10, 15),
        )

        booking = update_booking(
            booking,
            car=expensive_car,
        )

        self.assertEqual(
            booking.total_price,
            Decimal("1000.00"),
        )
