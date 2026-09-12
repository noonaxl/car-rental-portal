from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
            "role",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "role",
            "created_at",
            "updated_at",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "phone",
            "first_name",
            "last_name",
        ]

    def validate(self, attrs):
        if "role" in self.initial_data:
            raise serializers.ValidationError(
                {
                    "role": (
                        "You cannot set your role "
                        "during registration."
                    )
                }
            )

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            role=User.Role.USER,
            **validated_data,
        )

        return user
