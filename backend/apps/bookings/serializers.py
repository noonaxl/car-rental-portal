from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    def validate_year(self, value):
        if value < 2000:
            raise serializers.ValidationError(
                "Invalid year"
            )

        return value
