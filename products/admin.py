"""products app models."""
from django.contrib import admin
from .models import (
    Product,
    ProductVariant,
    Stock,
)

admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Stock)
