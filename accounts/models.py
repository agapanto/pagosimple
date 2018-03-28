"""accounts app models."""
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
    # NAME_FIELD_MAX_LENGTH,
)


class Account(ActiveModelMixin, EnabledModelMixin, PerAppModelMixin,
              TrackableModelMixin, UniqueIDModelMixin):
    """
    Account model.

    This model represents the Account of an user in the system.
    """

    customer_id = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    email = models.EmailField()
    metadata = JSONField()

    class Meta:
        """
        Set contraints to only allow the following.

        - One account email per App
        - One account customer_id per App
        """

        unique_together = (("email", "app"), ('customer_id', 'app'))

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.id)+" - "+str(self.created_at)
