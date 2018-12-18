"""payments app models."""
import logging
# from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.postgres.fields import (
    JSONField,
)
from rest_framework_apicontrol.mixins import (
    # ActiveModelMixin,
    # EnabledModelMixin,
    PerAppModelMixin,
    StatusModelMixin,
    TrackableModelMixin,
    UniqueIDModelMixin,
)
from accounts.models import (
    Account,
)
from products.models import (
    ProductVariant,
)

logger = logging.getLogger(__name__)

STATUS_FIELD_MAX_LENGTH = 32
TYPE_FIELD_MAX_LENGTH = 32
PAYMENT_STATUS_CHOICES = (
    ('created', 'created'),
    ('cancelled_by_user', 'cancelled_by_user'),
    ('cancelled_by_timeout', 'cancelled_by_timeout'),
    ('cancelled_by_gateway', 'cancelled_by_gateway'),
    ('completed', 'completed'),
)
PAYMENT_TYPE_CHOICES = (
    ('single_payment', 'single_payment'),
    ('plan_subscription', 'plan_subscription'),
    ('plan_renewal', 'plan_renewal'),
    ('products_order', 'products_order'),
)

# TODO: Payment checker "CRON" to check Payments and cancel them by timeout


class Payment(PerAppModelMixin,
              StatusModelMixin,
              TrackableModelMixin,
              UniqueIDModelMixin):
    """
    Payment model.

    Represents a Payment in an specific app.
    """

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    payment_status = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=PAYMENT_STATUS_CHOICES
    )
    payment_type = models.CharField(
        max_length=TYPE_FIELD_MAX_LENGTH,
        choices=PAYMENT_TYPE_CHOICES
    )
    metadata = JSONField(
        default=dict,
        blank=True
    )

    def __str__(self):
        """Return the class instance item name in django admin."""
        return "{unique_id} - {status}".format(
            unique_id=self.unique_id,
            status=self.payment_status
        )
