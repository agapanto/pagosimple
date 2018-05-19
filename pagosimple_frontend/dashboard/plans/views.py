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


class PlanListView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/plans/list.html')

        app_unique_id = kwargs.get('app_unique_id')
        app = App.objects.get(unique_id=app_unique_id)
        plans = Plan.objects.filter(app=app).order_by(
            '-updated_at'
        )

        context = {
            'app_unique_id': app_unique_id,
            'app': app,
            'plans': plans
        }

        return HttpResponse(template.render(context, request))


class PlanDetailView(View):
    def get(self, request, *args, **kwargs):
        """It is the main view of the dashboard."""
        template = loader.get_template('dashboard/apps/plans/detail.html')

        app_unique_id = kwargs.get('app_unique_id')
        plan_unique_id = kwargs.get('plan_unique_id')

        app = App.objects.get(unique_id=app_unique_id)
        plans = Plan.objects.filter(app=app)
        plan = Plan.objects.get(unique_id=plan_unique_id)

        context = {
            'app_unique_id': app_unique_id,
            'app': app,
            'plans': plans,
            'plan': plan,
            'plan_instances': plan.planinstance_set.all().order_by(
                '-created_at'
            )
        }

        return HttpResponse(template.render(context, request))


class PlanCreateView(CreateView):
    template_name = 'dashboard/apps/plans/create.html'
    form_class = PlanForm
    model = Plan

    def get_context_data(self, **kwargs):
        context = super(PlanCreateView, self).get_context_data(
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
            'app_detail_plan_list',
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

        form.instance.app = app

        return super().form_valid(form)

    def get_initial(self, **kwargs):
        """Set initial value of Form fields."""
        initial_data = super(PlanCreateView, self).get_initial(
            **kwargs
        )

        app_unique_id = self.kwargs.get('app_unique_id')
        app = App.objects.get(unique_id=app_unique_id)

        initial_data['code'] = 'PLAN{correlative}'.format(
            correlative=str(
                Plan.objects.filter(app=app).count() + 1
            )
        )

        return initial_data


class PlanEditView(UpdateView):
    template_name = 'dashboard/apps/plans/edit.html'
    form_class = PlanForm
    model = Plan

    def get_object(self, **kwargs):
        plan_unique_id = self.kwargs.get('plan_unique_id')

        return self.model.objects.get(unique_id=plan_unique_id)

    def get_context_data(self, **kwargs):
        context = super(PlanEditView, self).get_context_data(
            **kwargs
        )

        app_unique_id = self.kwargs.get('app_unique_id')

        app = App.objects.get(unique_id=app_unique_id)

        context['app_unique_id'] = app_unique_id
        context['app'] = app
        context['plan_instances'] = self.get_object().planinstance_set.all().order_by(
            '-created_at'
        )

        return context

    def get_success_url(self, **kwargs):
        """If form is valid, return the user to Plan detail view."""
        success_url = reverse(
            'app_detail_plan_detail',
            kwargs={
                'app_unique_id': self.kwargs.get('app_unique_id'),
                'plan_unique_id': self.kwargs.get('plan_unique_id'),
            }
        )

        return success_url
