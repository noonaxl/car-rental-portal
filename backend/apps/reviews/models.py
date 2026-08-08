from django.db import models

from apps.bookings.models import Booking
from apps.cars.models import Car
from apps.users.models import User


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="review",
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Review #{self.id} — {self.rating}/5"
