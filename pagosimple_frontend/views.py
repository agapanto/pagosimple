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
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from rest_framework_apicontrol.models import (
    App,
)
from plans.models import (
    Plan,
)
from plans.forms import (
    PlanForm,
)

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    """It is the main view of the pagosimple_frontend app."""
    template = loader.get_template('index.html')

    context = {
        'message': 'Welcome to pagosimple',
    }

    return HttpResponse(template.render(context, request))


class DashboardBriefView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/brief.html')

        context = {
        }

        return HttpResponse(template.render(context, request))


class DashboardAppView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/detail.html')

        app_unique_id = kwargs.get('app_unique_id')
        app = App.objects.get(unique_id=app_unique_id)

        context = {
            'app_unique_id': app_unique_id,
            'app': app
        }

        return HttpResponse(template.render(context, request))
