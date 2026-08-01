from django.contrib import admin

from .models import Car, CarImage, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "brand",
        "model",
        "year",
        "price_per_day",
        "category",
    )

    list_filter = (
        "category",
        "year",
    )

    search_fields = (
        "brand",
        "model",
    )


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "car",
        "image",
    )
