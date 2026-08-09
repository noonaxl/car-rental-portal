from django.utils import timezone
from rest_framework import serializers

from .models import Booking
from .services import create_booking, update_booking


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

    def validate_start_date(self, value):
        if value < timezone.localdate():
            raise serializers.ValidationError(
                "Start date cannot be in the past."
            )

        return value

    def validate(self, attrs):
        start_date = attrs.get(
            "start_date",
            self.instance.start_date if self.instance else None,
        )

        end_date = attrs.get(
            "end_date",
            self.instance.end_date if self.instance else None,
        )

        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError(
                {
                    "end_date": (
                        "End date must be later than start date."
                    )
                }
            )

        return attrs

    def create(self, validated_data):
        return create_booking(**validated_data)

    def update(self, instance, validated_data):
        return update_booking(
            instance,
            **validated_data,
        )
