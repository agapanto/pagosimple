"""pagosimple_frontend app views."""
# import os
import logging
from django.http import (
    HttpResponse,
    # HttpResponseRedirect,
)
from django.template import loader
from django.urls import reverse
from django.views import View
from django.views.generic import (
    # DetailView,
    # FormView,
    CreateView,
    UpdateView,
    # DeleteView,
    # ListView,
)
from rest_framework_apicontrol.models import (
    App,
)
from payments.models import (
    Payment,
)
from payments.forms import (
    PaymentForm,
)

logger = logging.getLogger(__name__)


# Plan model related views
class PaymentListView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/payments/list.html')

        app_unique_id = kwargs.get('app_unique_id')
        app = App.objects.get(unique_id=app_unique_id)
        payments = Payment.objects.filter(app=app).order_by(
            '-updated_at'
        )

        context = {
            'app_unique_id': app_unique_id,
            'app': app,
            'payments': payments
        }

        return HttpResponse(template.render(context, request))


class PaymentDetailView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/payments/detail.html')

        app_unique_id = kwargs.get('app_unique_id')
        payment_unique_id = kwargs.get('payment_unique_id')

        app = App.objects.get(unique_id=app_unique_id)
        payment = Payment.objects.get(unique_id=payment_unique_id)

        context = {
            'app_unique_id': app_unique_id,
            'app': app,
            'payment': payment
        }

        return HttpResponse(template.render(context, request))

