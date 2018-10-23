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
from accounts.models import (
    Account
)


class AccountForm(ModelForm):
    """accounts.Account model form."""

    class Meta:
        model = Account
        fields = [
            # 'app',
            # 'created_at',
            # 'updated_at',
            'customer_id',
            'email',
            # 'metadata',
            'enabled',
        ]
