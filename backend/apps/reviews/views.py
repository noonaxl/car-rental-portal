from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.select_related(
        "user",
        "car",
        "booking",
    ).all()

    serializer_class = ReviewSerializer

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "comment",
        "car__brand",
        "car__model",
        "user__username",
    ]

    ordering_fields = [
        "rating",
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]
