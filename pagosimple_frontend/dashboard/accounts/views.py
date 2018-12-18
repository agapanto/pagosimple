"""pagosimple_frontend app views."""
# import os
import logging
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404
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
from accounts.models import (
    Account,
)
from accounts.forms import (
    AccountForm,
)

logger = logging.getLogger(__name__)


# Account model related views
class AccountListView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/accounts/list.html')

        app_unique_id = kwargs.get('app_unique_id')
        app = App.objects.get(unique_id=app_unique_id)
        accounts = Account.objects.filter(app=app).order_by(
            '-created_at'
        )

        context = {
            'app_unique_id': app_unique_id,
            'app': app,
            'accounts': accounts
        }

        return HttpResponse(template.render(context, request))


class AccountDetailView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/accounts/detail.html')

        app_unique_id = kwargs.get('app_unique_id')
        account_unique_id = kwargs.get('account_unique_id')

        app = App.objects.get(unique_id=app_unique_id)
        account = Account.objects.get(unique_id=account_unique_id)

        context = {
            'app_unique_id': app_unique_id,
            'app': app,
            'account': account,
        }

        return HttpResponse(template.render(context, request))


class AccountCreateView(CreateView):
    template_name = 'dashboard/apps/accounts/create.html'
    form_class = AccountForm
    model = Account

    def get_context_data(self, **kwargs):
        context = super(AccountCreateView, self).get_context_data(
            **kwargs
        )

        app_unique_id = self.kwargs.get('app_unique_id')

        app = App.objects.get(unique_id=app_unique_id)

        context['app_unique_id'] = app_unique_id
        context['app'] = app

        return context

    def get_success_url(self, **kwargs):
        """If form is valid, return the user to Account detail view."""
        success_url = reverse(
            'app_detail_account_list',
            kwargs={
                'app_unique_id': self.kwargs.get('app_unique_id')
            }
        )

        return success_url

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.

        After form validation, if it's valid, set the current app relationship
        to the PlanForm.
        """
        context = self.get_context_data()
        app = context.get('app')

        # form.instance.app = app

        return super().form_valid(form)

    def get_initial(self, **kwargs):
        """Set initial value of Form fields."""
        initial_data = super(AccountCreateView, self).get_initial(
            **kwargs
        )

        app_unique_id = self.kwargs.get('app_unique_id')
        app = App.objects.get(unique_id=app_unique_id)

        initial_data['app'] = app

        return initial_data


class AccountEditView(UpdateView):
    template_name = 'dashboard/apps/accounts/edit.html'
    form_class = AccountForm
    model = Account

    def get_object(self, **kwargs):
        account_unique_id = self.kwargs.get('account_unique_id')

        return self.model.objects.get(unique_id=account_unique_id)

    def get_context_data(self, **kwargs):
        context = super(AccountEditView, self).get_context_data(
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
            'app_detail_account_detail',
            kwargs={
                'app_unique_id': self.kwargs.get('app_unique_id'),
                'account_unique_id': self.kwargs.get('account_unique_id'),
            }
        )

        return success_url


class AccountArchiveView(View):

    def get(self, request, app_unique_id, account_unique_id):

        account = get_object_or_404(
            Account,
            unique_id=account_unique_id
        )

        account.archive_status(commit=False)
        account.disable(commit=False)
        account.save()

        account_url = reverse(
            'app_detail_account_detail',
            kwargs={
                'app_unique_id': app_unique_id,
                'account_unique_id': account_unique_id,
            }
        )

        return HttpResponseRedirect(
            account_url
        )
