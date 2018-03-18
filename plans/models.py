import logging
import uuid
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import (
    JSONField,
)
from rest_framework_apicontrol.mixins import (
    TrackableModelMixin,
    UniqueIDModelMixin,
)
from rest_framework_apicontrol.models import (
    CODE_FIELD_MAX_LENGTH,
    NAME_FIELD_MAX_LENGTH,
    App,
)


RENEWAL_PERIOD_TYPE_CHOICES = (
    ('hours', 'hours'),
    ('days', 'days'),
    ('weeks', 'weeks'),
    ('months', 'months'),
    ('years', 'years'),
)

logger = logging.getLogger(__name__)


class Plan(TrackableModelMixin, UniqueIDModelMixin):
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
    enabled = models.BooleanField(
        default=False
    )
    app = models.ForeignKey(
        App,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("code", "app"),)

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)


class PlanInstance(TrackableModelMixin, UniqueIDModelMixin):
    """
    Plan Instance model.

    Represents an specific Plan instance for a user account.
    """

    active = models.BooleanField(
        default=False
    )
    renewal_datetime = models.DateTimeField()

    metadata = JSONField()

    plan = models.ForeignKey(
        Plan,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def set_renewal_datetime(self, period_count, period_type):
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
        return str(self.id)


class RenewalOption(TrackableModelMixin, UniqueIDModelMixin):
    """
    Renewal Option model.

    Represents an option for pay and extend a PlanInstance renewal_datetime
    based on the Plan price.
    """

    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    discount = models.FloatField(
        default=0
    )
    active = models.BooleanField(
        default=False
    )
    renewal_period_count = models.IntegerField(
        default=1
    )
    renewal_period_type = models.CharField(
        choices=RENEWAL_PERIOD_TYPE_CHOICES,
        default='months',
        max_length=100
    )
    plan = models.ForeignKey(
        Plan,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.name)+" - "+str(self.created_at)
