"""plans app forms."""
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
            # 'app',
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
