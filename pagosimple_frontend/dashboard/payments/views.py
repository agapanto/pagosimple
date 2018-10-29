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


class PaymentCreateView(CreateView):
    template_name = 'dashboard/apps/payments/create.html'
    form_class = PaymentForm
    model = Payment

    def get_context_data(self, **kwargs):
        context = super(PaymentCreateView, self).get_context_data(
            **kwargs
        )

        app_unique_id = self.kwargs.get('app_unique_id')

        app = App.objects.get(unique_id=app_unique_id)

        context['app_unique_id'] = app_unique_id
        context['app'] = app

        return context

    def get_success_url(self, **kwargs):
        """If form is valid, return the user to Plan detail view."""
        success_url = reverse(
            'app_detail_payments_list',
            kwargs={
                'app_unique_id': self.kwargs.get('app_unique_id')
            }
        )

        return success_url

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.

        After form validation, if it's valid, set the current app relationship
        to the PaymentForm.
        """
        context = self.get_context_data()
        app = context.get('app')

        form.instance.app = app

        return super().form_valid(form)

    def get_initial(self, **kwargs):
        """Set initial value of Form fields."""
        initial_data = super(PaymentCreateView, self).get_initial(
            **kwargs
        )

        initial_data['status'] = 'created'
        initial_data['payment_type'] = 'single_payment'

        return initial_data


class PaymentEditView(UpdateView):
    template_name = 'dashboard/apps/payments/edit.html'
    form_class = PaymentForm
    model = Payment

    def get_object(self, **kwargs):
        payment_unique_id = self.kwargs.get('payment_unique_id')

        return self.model.objects.get(unique_id=payment_unique_id)

    def get_context_data(self, **kwargs):
        context = super(PaymentEditView, self).get_context_data(
            **kwargs
        )

        app_unique_id = self.kwargs.get('app_unique_id')

        app = App.objects.get(unique_id=app_unique_id)

        context['app_unique_id'] = app_unique_id
        context['app'] = app

        return context

    def get_success_url(self, **kwargs):
        """If form is valid, return the user to Plan detail view."""
        success_url = reverse(
            'app_detail_payments_detail',
            kwargs={
                'app_unique_id': self.kwargs.get('app_unique_id'),
                'payment_unique_id': self.kwargs.get('payment_unique_id'),
            }
        )

        return success_url
