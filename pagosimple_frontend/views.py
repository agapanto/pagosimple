"""pagosimple_frontend app views."""
# import os
import logging
from django.http import (
    HttpResponse,
    # HttpResponseRedirect,
)
from django.template import loader

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    """It is the main view of the pagosimple_frontend app."""
    template = loader.get_template('index.html')

    context = {
        'message': 'Welcome to pagosimple',
    }

    return HttpResponse(template.render(context, request))


def dashboard_brief(request, *args, **kwargs):
    """It is the main view of the dashboard."""
    template = loader.get_template('dashboard/brief.html')

    context = {
    }

    return HttpResponse(template.render(context, request))


def app_detail(request, *args, **kwargs):
    """It is the main view of the dashboard."""
    template = loader.get_template('dashboard/apps/detail.html')

    context = {
    }

    return HttpResponse(template.render(context, request))
