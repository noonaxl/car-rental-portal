import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestUsersAPI:

    def setup_method(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="apiuser",
            email="api@example.com",
            password="StrongPassword123",
        )

    def test_me_requires_authentication(self):
        response = self.client.get(
            "/api/v1/users/me/",
        )

        assert response.status_code == 401

    def test_me_returns_current_user(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.get(
            "/api/v1/users/me/",
        )

        assert response.status_code == 200
        assert response.data["id"] == self.user.id
        assert response.data["username"] == "apiuser"
        assert response.data["email"] == "api@example.com"

        assert "password" not in response.data

    def test_user_cannot_change_role(self):
        self.client.force_authenticate(
            user=self.user,
        )

        response = self.client.patch(
            f"/api/v1/users/{self.user.id}/",
            {
                "role": "admin",
            },
            format="json",
        )

        assert response.status_code == 405

        self.user.refresh_from_db()

        assert self.user.role == "user"
