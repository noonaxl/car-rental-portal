from django.utils import timezone
from rest_framework import serializers

from .models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = [
            "id",
            "image",
        ]


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Car
        fields = [
            "id",
            "brand",
            "model",
            "year",
            "price_per_day",
            "category",
            "images",
        ]
        read_only_fields = [
            "id",
            "images",
        ]

    def validate_price_per_day(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price per day must be greater than 0."
            )
        return value

    def validate_year(self, value):
        current_year = timezone.now().year

        if value < 1900 or value > current_year:
            raise serializers.ValidationError(
                f"Year must be between 1900 and {current_year}."
            )

        return value
