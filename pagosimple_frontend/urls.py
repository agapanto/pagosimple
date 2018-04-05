"""pagosimple_frontend app urls."""
from django.conf.urls import (
    # include,
    url,
)
from django.contrib.auth import (
    views as auth_views,
)
from django.urls import(
    path,
    re_path,
)
from .views import (
    index,
    dashboard_brief,
    app_detail
)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/web'}, name='logout'),
    path('dashboard/apps', dashboard_brief, name='dashboard'),
    path('dashboard/apps/<uuid:app_unique_id>', app_detail, name='app_detail'),
]
