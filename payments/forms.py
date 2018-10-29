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
from payments.models import (
    Payment,
)


class PaymentForm(ModelForm):
    """plans.Plan model form."""

    class Meta:
        model = Payment
        fields = [
            # 'app',
            # 'created_at',
            # 'updated_at',
            'account',
            'status',
            'payment_type',
            'metadata',
        ]
