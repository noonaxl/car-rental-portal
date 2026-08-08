from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .filters import CarFilter
from .models import Car
from .serializers import CarSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all().order_by("id")
    serializer_class = CarSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = CarFilter

    search_fields = [
        "brand",
        "model",
    ]

    ordering_fields = [
        "price_per_day",
        "year",
    ]
