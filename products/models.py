"""plans app models."""
import logging
# from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone
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
from rest_framework_apicontrol.models import (
    CODE_FIELD_MAX_LENGTH,
    NAME_FIELD_MAX_LENGTH,
)

logger = logging.getLogger(__name__)


class BaseProduct(PerAppModelMixin,
                  TrackableModelMixin,
                  UniqueIDModelMixin):
    """
    BaseProduct model.

    Contains the common fields between Product and ProductVariant models.
    """

    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    slug = models.SlugField()

    class Meta:
        """Make the base model abstract."""

        abstract = True

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)


class Product(BaseProduct):
    """
    Product model.

    Represents a Plan in an specific app.
    """

    class Meta:
        """
        Set contraints to only allow the following.

        - One Product code per App
        """

        unique_together = (("code", "app"),)

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)


class ProductVariant(BaseProduct):
    """
    Product model.

    Represents a Plan in an specific app.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    class Meta:
        """
        Set contraints to only allow the following.

        - One ProductVariant code per App
        """

        unique_together = (("code", "app"),)

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)


class Stock(PerAppModelMixin,
            TrackableModelMixin,
            UniqueIDModelMixin):
    """
    Stock model.

    Represents the stock of a ProductVariant in an specific app.
    """

    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE
    )
    stock = models.IntegerField()
    valid_to = models.DateTimeField(
        default=timezone.now,
        help_text='Limit DateTime in which the Stock instance \'ll be valid.'
    )

    class Meta:
        """
        Set contraints to only allow the following.

        - One Stock per product_variant per App
        """

        unique_together = (("product_variant", "app"),)

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)
