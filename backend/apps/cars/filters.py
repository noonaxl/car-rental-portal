from django_filters import rest_framework as filters

from .models import Car


class CarFilter(filters.FilterSet):
    min_price = filters.NumberFilter(
        field_name="price_per_day",
        lookup_expr="gte"
    )

    max_price = filters.NumberFilter(
        field_name="price_per_day",
        lookup_expr="lte"
    )

    min_year = filters.NumberFilter(
        field_name="year",
        lookup_expr="gte"
    )

    max_year = filters.NumberFilter(
        field_name="year",
        lookup_expr="lte"
    )

    class Meta:
        model = Car

        fields = [
            "category",
            "brand",
            "year",
        ]
