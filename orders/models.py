"""orders app models."""
import logging
# from dateutil.relativedelta import relativedelta
from django.db import models
# from django.utils import timezone
# from django.contrib.postgres.fields import (
#     JSONField,
# )
from rest_framework_apicontrol.mixins import (
    # ActiveModelMixin,
    # EnabledModelMixin,
    PerAppModelMixin,
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
ORDER_STATUS_CHOICES = (
    ('created', 'created'),
    ('cancelled', 'cancelled'),
    ('cancelled_by_timeout', 'cancelled_by_timeout'),
    ('shipped', 'shipped'),
    ('delivered', 'delivered'),
)

# TODO: Order checker "CRON" to check Orders and cancel them by timeout


class Order(PerAppModelMixin,
            TrackableModelMixin,
            UniqueIDModelMixin):
    """
    Order model.

    Represents an Order in an specific app.
    """

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=STATUS_FIELD_MAX_LENGTH,
        choices=ORDER_STATUS_CHOICES
    )

    product_list = models.ManyToManyField(
        ProductVariant,
        through='OrderItem',
        help_text='Product list to set ProductVariant & their quantity\
                  in the Order'
    )

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)


class OrderItem(TrackableModelMixin,
                UniqueIDModelMixin):
    """
    OrderItem model.

    Represents one item in an Order in an specific app.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE
    )
    product_variant_quantity = models.IntegerField(
        default=0
    )

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)
