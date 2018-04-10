"""pagosimple_frontend app urls."""
from django.contrib.auth import (
    views as auth_views,
)
from django.urls import (
    path,
    # re_path,
)
from .views import (
    index,
    DashboardBriefView,
    DashboardAppView,
    DashboardAppPaymentsView,
)


urlpatterns = [
    path(
        '',
        index,
        name='index'
    ),
    path(
        'login',
        auth_views.login,
        name='login'
    ),
    path(
        'logout',
        auth_views.logout,
        {'next_page': '/web'},
        name='logout'
    ),
    path(
        'dashboard/apps',
        DashboardBriefView.as_view(),
        name='dashboard'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>',
        DashboardAppView.as_view(),
        name='app_detail'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/payments',
        DashboardAppPaymentsView.as_view(),
        name='app_detail_payments'
    ),
]
