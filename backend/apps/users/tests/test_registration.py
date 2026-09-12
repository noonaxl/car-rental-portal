import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestRegistration:

    def setup_method(self):
        self.client = APIClient()
        self.url = "/api/v1/users/register/"

    def test_register_user_success(self):
        response = self.client.post(
            self.url,
            {
                "username": "testuser",
                "email": "test@example.com",
                "password": "StrongPassword123",
                "phone": "+40123456789",
                "first_name": "Test",
                "last_name": "User",
            },
            format="json",
        )

        assert response.status_code == 201

        user = User.objects.get(username="testuser")

        assert user.email == "test@example.com"
        assert user.role == "user"
        assert user.check_password("StrongPassword123")

    def test_password_is_not_returned(self):
        response = self.client.post(
            self.url,
            {
                "username": "passwordtest",
                "email": "password@example.com",
                "password": "StrongPassword123",
            },
            format="json",
        )

        assert response.status_code == 201
        assert "password" not in response.data

    def test_short_password_rejected(self):
        response = self.client.post(
            self.url,
            {
                "username": "shortpassword",
                "email": "short@example.com",
                "password": "123",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_invalid_email_rejected(self):
        response = self.client.post(
            self.url,
            {
                "username": "invalidemail",
                "email": "not-an-email",
                "password": "StrongPassword123",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_duplicate_username_rejected(self):
        User.objects.create_user(
            username="existing",
            email="existing@example.com",
            password="StrongPassword123",
        )

        response = self.client.post(
            self.url,
            {
                "username": "existing",
                "email": "new@example.com",
                "password": "StrongPassword123",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_duplicate_email_rejected(self):
        User.objects.create_user(
            username="user1",
            email="same@example.com",
            password="StrongPassword123",
        )

        response = self.client.post(
            self.url,
            {
                "username": "user2",
                "email": "same@example.com",
                "password": "StrongPassword123",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_role_cannot_be_set_during_registration(self):
        response = self.client.post(
            self.url,
            {
                "username": "hacker",
                "email": "hacker@example.com",
                "password": "StrongPassword123",
                "role": "admin",
            },
            format="json",
        )

        assert response.status_code == 400

        assert not User.objects.filter(
            username="hacker",
            role="admin",
        ).exists()
