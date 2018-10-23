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

