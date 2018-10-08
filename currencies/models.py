"""currencies app models."""
from django.db import models
from django.db.models.signals import pre_save
from rest_framework_apicontrol.mixins import (
    # ActiveModelMixin,
    EnabledModelMixin,
    # PerAppModelMixin,
    TrackableModelMixin,
    # UniqueIDModelMixin,
)
from django.core.exceptions import (
    ObjectDoesNotExist,
)


class Currency(EnabledModelMixin, TrackableModelMixin):
    """
    Currency model.

    This represents a currency managed by the system.
    """

    name = models.CharField(
        max_length=100
    )
    symbol = models.CharField(
        max_length=3
    )
    code = models.CharField(
        max_length=10,
        primary_key=True
    )

    conversion_factor = models.FloatField(
        default=1
    )

    def calculate_as(self, currency_code, amount=1):
        """
        Calculate the value of current currency another currency.

        Args:
            currency_code: The code of the currency to calculate to.
            amount: The amount in units of the current currency to calculate in
                the destination currency.

        Return:
            The calculated value of the new currency multiplied by the amount
            of the current(self) currency.

        Raise:
            ObjectDoesNotExist: The currency with the requested currency_code
                does not exist.
        """
        try:
            destination_currency = Currency.objects.get(
                code=currency_code
            )

            value = amount * destination_currency.conversion_factor / self.conversion_factor

            return value

        except ObjectDoesNotExist as e:
            raise

    def __str__(self):
        return "{name} - {code}".format(
            name=self.name,
            code=self.code
        )


class CurrencyValue(TrackableModelMixin):
    """
    Currency value model.

    This represents the value of a currency on a specific datetime.
    """

    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE
    )
    value = models.FloatField()
    datetime = models.DateTimeField()

    def __str__(self):
        return "{name} - {value}".format(
            name=self.currency.name,
            value=self.value
        )


# Signals
def uppercase_code(sender, instance, **kwargs):
    instance.code = instance.code.upper()


pre_save.connect(uppercase_code, sender=Currency)
