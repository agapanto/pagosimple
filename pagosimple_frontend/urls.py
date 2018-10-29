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
)
from .dashboard.payments.views import (
    # Payment model views
    PaymentListView,
    PaymentDetailView,
)
from .dashboard.plans.views import (
    # Plan model views
    PlanListView,
    PlanCreateView,
    PlanDetailView,
    PlanEditView,
    # PlanInstance model views
    PlanInstanceDetailView,
    PlanInstanceEditView,
    PlanInstanceCreateView,
)

from .dashboard.accounts.views import (
    # Account model views
    AccountListView,
    AccountDetailView,
    AccountCreateView,
    AccountEditView,
)


urlpatterns = [
    path(
        '',
        index,
        name='index'
    ),
    path(
        'login',
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout',
        auth_views.LogoutView.as_view(),
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
    # Payment model views
    path(
        'dashboard/apps/<uuid:app_unique_id>/payments',
        PaymentListView.as_view(),
        name='app_detail_payments_list'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/payments/<uuid:payment_unique_id>',
        PaymentDetailView.as_view(),
        name='app_detail_payments_detail'
    ),
    # Plan model views
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans',
        PlanListView.as_view(),
        name='app_detail_plan_list'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans/new',
        PlanCreateView.as_view(),
        name='app_detail_plan_create'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans/<uuid:plan_unique_id>',
        PlanDetailView.as_view(),
        name='app_detail_plan_detail'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans/<uuid:plan_unique_id>/edit',
        PlanEditView.as_view(),
        name='app_detail_plan_edit'
    ),
    # PlanInstance model views
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans/<uuid:plan_unique_id>/subscriptions/<uuid:plan_instance_unique_id>',
        PlanInstanceDetailView.as_view(),
        name='app_detail_plan_planinstance_detail'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans/<uuid:plan_unique_id>/subscriptions/<uuid:plan_instance_unique_id>/edit',
        PlanInstanceEditView.as_view(),
        name='app_detail_plan_planinstance_edit'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/plans/<uuid:plan_unique_id>/subscriptions/new',
        PlanInstanceCreateView.as_view(),
        name='app_detail_plan_planinstance_create'
    ),
    # Account model views
    path(
        'dashboard/apps/<uuid:app_unique_id>/accounts',
        AccountListView.as_view(),
        name='app_detail_account_list'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/accounts/<uuid:account_unique_id>',
        AccountDetailView.as_view(),
        name='app_detail_account_detail'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/accounts/create',
        AccountCreateView.as_view(),
        name='app_detail_account_create'
    ),
    path(
        'dashboard/apps/<uuid:app_unique_id>/accounts/<uuid:account_unique_id>/edit',
        AccountEditView.as_view(),
        name='app_detail_account_edit'
    ),
]
