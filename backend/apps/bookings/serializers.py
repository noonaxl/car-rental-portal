from django.utils import timezone
from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "user",
            "car",
            "start_date",
            "end_date",
            "status",
            "total_price",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "total_price",
            "created_at",
        ]

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError(
                {
                    "end_date": (
                        "End date must be later than start date."
                    )
                }
            )

        if start_date and start_date < timezone.localdate():
            raise serializers.ValidationError(
                {
                    "start_date": (
                        "Start date cannot be in the past."
                    )
                }
            )

        return attrs

    def create(self, validated_data):
        car = validated_data["car"]
        start_date = validated_data["start_date"]
        end_date = validated_data["end_date"]

        days = (end_date - start_date).days
        total_price = car.price_per_day * days

        return Booking.objects.create(
            total_price=total_price,
            **validated_data,
        )

    def update(self, instance, validated_data):
        car = validated_data.get("car", instance.car)
        start_date = validated_data.get(
            "start_date",
            instance.start_date,
        )
        end_date = validated_data.get(
            "end_date",
            instance.end_date,
        )

        days = (end_date - start_date).days
        validated_data["total_price"] = (
                car.price_per_day * days
        )

        return super().update(
            instance,
            validated_data,
        )
