from django.forms import (
    # Form,
    ModelForm,
)
from django.utils import (
    timezone,
)
from rest_framework_apicontrol.models import (
    App,
)
from plans.models import (
    Plan,
)


class PlanForm(ModelForm):
    """plans.Plan model form."""

    class Meta:
        model = Plan
        fields = [
            'enabled',
            # 'app',
            # 'created_at',
            # 'updated_at',
            'code',
            'name',
        ]
