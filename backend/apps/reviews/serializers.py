from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "car",
            "booking",
            "rating",
            "comment",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )

        return value

    def validate(self, attrs):
        user = attrs.get("user")
        car = attrs.get("car")
        booking = attrs.get("booking")

        if booking:
            if booking.user_id != user.id:
                raise serializers.ValidationError(
                    {
                        "booking": (
                            "This booking does not belong "
                            "to the selected user."
                        )
                    }
                )

            if booking.car_id != car.id:
                raise serializers.ValidationError(
                    {
                        "car": (
                            "This car does not belong "
                            "to the selected booking."
                        )
                    }
                )

            if booking.status != "completed":
                raise serializers.ValidationError(
                    {
                        "booking": (
                            "A review can only be created "
                            "for a completed booking."
                        )
                    }
                )

        return attrs
