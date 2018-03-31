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
        'message': 'hello world pagosimple',
    }

    return HttpResponse(template.render(context, request))
