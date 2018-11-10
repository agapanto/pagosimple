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
from accounts.models import (
    Account
)


class AccountForm(ModelForm):
    """accounts.Account model form."""

    class Meta:
        model = Account
        fields = [
            'app',
            # 'created_at',
            # 'updated_at',
            'customer_id',
            'email',
            # 'metadata',
            'enabled',
        ]
        widgets = {
            'app': forms.HiddenInput()
        }

    def clean_customer_id(self):
        """Validate & clean the customer_id form field."""
        # Get data to look at
        customer_id = self.cleaned_data["customer_id"]
        app = self.cleaned_data["app"]

        query_args = {
            'customer_id': customer_id,
            'app': app
        }

        if Account.objects.filter(**query_args).exists():
            # Get the existant model instance
            existant_account = Account.objects.get(**query_args)

            # Compare if the current instance model is the one is saved in DB
            if self.instance.pk != existant_account.pk:
                raise ValidationError(
                    'An Account with this customer id already exists in current App.'
                )

        return customer_id

    def clean_email(self):
        """Validate & clean the email form field."""
        # Get data to look at
        email = self.cleaned_data["email"]
        app = self.cleaned_data["app"]

        query_args = {
            'email': email,
            'app': app
        }

        if Account.objects.filter(**query_args).exists():
            # Get the existant model instance
            existant_account = Account.objects.get(**query_args)

            # Compare if the current instance model is the one is saved in DB
            if self.instance.pk != existant_account.pk:
                raise ValidationError(
                    'An Account with this email already exists in current App.'
                )

        return email
