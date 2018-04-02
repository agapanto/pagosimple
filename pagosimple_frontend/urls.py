"""pagosimple_frontend app urls."""
from django.conf.urls import (
    # include,
    url,
)
from django.contrib.auth import (
    views as auth_views,
)
from .views import (
    index,
    dashboard_brief,
)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/web'}, name='logout'),
    url(r'^dashboard/$', dashboard_brief, name='dashboard'),
]
