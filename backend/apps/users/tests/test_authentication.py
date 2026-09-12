import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestAuthentication:

    def setup_method(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="jwtuser",
            email="jwt@example.com",
            password="StrongPassword123",
        )

    def test_login_returns_tokens(self):
        response = self.client.post(
            "/api/v1/users/login/",
            {
                "username": "jwtuser",
                "password": "StrongPassword123",
            },
            format="json",
        )

        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data

    def test_wrong_password_rejected(self):
        response = self.client.post(
            "/api/v1/users/login/",
            {
                "username": "jwtuser",
                "password": "WrongPassword123",
            },
            format="json",
        )

        assert response.status_code == 401

    def test_refresh_token_returns_access_token(self):
        login_response = self.client.post(
            "/api/v1/users/login/",
            {
                "username": "jwtuser",
                "password": "StrongPassword123",
            },
            format="json",
        )

        refresh_token = login_response.data["refresh"]

        response = self.client.post(
            "/api/v1/users/token/refresh/",
            {
                "refresh": refresh_token,
            },
            format="json",
        )

        assert response.status_code == 200
        assert "access" in response.data
