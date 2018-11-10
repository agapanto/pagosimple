"""plans app forms."""
from django import forms
from django.core.exceptions import (
    ValidationError,
)
from django.forms import (
    # Form,
    ModelForm,
)
# from django.utils import (
#     timezone,
# )
# from rest_framework_apicontrol.models import (
#     App,
# )
from plans.models import (
    Plan,
    PlanInstance,
)


class PlanForm(ModelForm):
    """plans.Plan model form."""

    class Meta:
        model = Plan
        fields = [
            'app',
            # 'created_at',
            # 'updated_at',
            'code',
            'name',
            'description',
            'base_price',
            'currency',
            'renewal_options',
            'enabled',
        ]
        widgets = {
            'app': forms.HiddenInput()
        }

    def clean_code(self):
        """Validate & clean the code form field."""
        # Get data to look at
        code = self.cleaned_data["code"]
        app = self.cleaned_data["app"]

        query_args = {
            'code': code,
            'app': app
        }

        if Plan.objects.filter(**query_args).exists():
            # Get the existant model instance
            existant_plan = Plan.objects.get(**query_args)

            # Compare if the current instance model is the one is saved in DB
            if self.instance.pk != existant_plan.pk:
                raise ValidationError(
                    'A Plan with this code already exists in current App.'
                )

        return code


class PlanInstanceForm(ModelForm):
    """plans.Plan model form."""

    class Meta:
        model = PlanInstance
        fields = [
            # 'app',
            # 'unique_id',
            # 'created_at',
            # 'updated_at',
            'renewal_datetime',
            # 'metadata',
            'plan',
            'account',
            'active',
        ]
