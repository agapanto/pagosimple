"""plans app models."""
import logging
from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.postgres.fields import (
    JSONField,
)
from rest_framework_apicontrol.mixins import (
    ActiveModelMixin,
    EnabledModelMixin,
    PerAppModelMixin,
    TrackableModelMixin,
    UniqueIDModelMixin,
)
from rest_framework_apicontrol.models import (
    CODE_FIELD_MAX_LENGTH,
    NAME_FIELD_MAX_LENGTH,
)


RENEWAL_PERIOD_TYPE_CHOICES = (
    ('hours', 'hours'),
    ('days', 'days'),
    ('weeks', 'weeks'),
    ('months', 'months'),
    ('years', 'years'),
)

logger = logging.getLogger(__name__)


class PlanGroup(PerAppModelMixin,
                TrackableModelMixin,
                UniqueIDModelMixin):
    """
    PlanGroup model.

    Useful to manage few RenewalOptions in database and reuse it.
    """

    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )

    class Meta:
        """
        Set contraints to only allow the following.

        - One account PlanGroup code per App
        """

        unique_together = (("code", "app"),)

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)


class Plan(EnabledModelMixin,
           PerAppModelMixin,
           TrackableModelMixin,
           UniqueIDModelMixin):
    """
    Plan model.

    Represents a Plan in an specific app.
    """

    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    base_price = models.FloatField(
        default=0
    )
    currency = models.ForeignKey(
        'currencies.Currency',
        on_delete=models.CASCADE,
        default='USD'
    )
    renewal_options = models.ManyToManyField(
        'plans.RenewalOption',
        blank=True
    )

    class Meta:
        """
        Set contraints to only allow the following.

        - One account Plan code per App
        """

        unique_together = (("code", "app"),)

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)


class PlanInstance(ActiveModelMixin, TrackableModelMixin, UniqueIDModelMixin):
    """
    Plan Instance model.

    Represents an specific Plan instance for a user account.
    """

    renewal_datetime = models.DateTimeField()

    metadata = JSONField(
        default={},
        blank=True
    )

    plan = models.ForeignKey(
        Plan,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def apply_renewal_option(self, obj, renewal_option, commit=True):
        """Apply an specific renewal_option to the current instance."""
        self.set_renewal_datetime(
            period_count=renewal_option.period_type,
            period_type=renewal_option.period_type,
            commit=False
        )

        if commit:
            obj.save()

    def set_renewal_datetime(self, obj, period_count, period_type,
                             commit=True):
        """Set an arbitrary renewal_datetime."""
        old_datetime = self.renewal_datetime

        parameters = {
            str(period_type): int(period_count)
        }

        relative_timedelta = relativedelta(**parameters)

        self.renewal_datetime = old_datetime + relative_timedelta

        logger.debug(
            'renewal_datetime for PlanInstance with id {}, changed from {}\
            to {}'.format(
                self.id,
                old_datetime,
                self.renewal_datetime
            )
        )

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.id)


class RenewalOption(ActiveModelMixin, TrackableModelMixin, UniqueIDModelMixin):
    """
    Renewal Option model.

    Represents an option for pay and extend a PlanInstance renewal_datetime
    based on the Plan price.
    """

    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    discount = models.FloatField(
        default=0
    )
    renewal_period_count = models.IntegerField(
        default=1
    )
    renewal_period_type = models.CharField(
        choices=RENEWAL_PERIOD_TYPE_CHOICES,
        default='months',
        max_length=12  # 12 for MILLENIALS
    )
    # plan_group = models.ForeignKey(
    #     PlanGroup,
    #     blank=True,
    #     null=True,
    #     on_delete=models.CASCADE
    # )

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.name)+" - "+str(self.created_at)
