"""Plans app models."""
from django.contrib import admin
from .models import (
    Plan,
    PlanInstance,
    RenewalOption,
)

admin.site.register(Plan)
admin.site.register(PlanInstance)
admin.site.register(RenewalOption)
