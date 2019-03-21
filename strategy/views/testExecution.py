# coding=utf-8
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from strategy.models.testExecution import TestExecution
from strategy.models.application import Application
from strategy.models.applicationScript import ApplicationScript
from strategy.models.testPlan import TestPlan
from strategy.models.applicationType import ApplicationType
from strategy.models.testStrategy import TestStrategy


@method_decorator(login_required(), name='dispatch')
class TestExecutionList(ListView):
    model = TestExecution
    template_name = 'TSDC/execution-detail.html'
    paginate_by = 20
    context_object_name = 'executions'

    def get_queryset(self):
        object_list = self.model.objects.filter(user=self.request.user)
        return object_list


def executionFind(request):
    apps = request.GET.getlist('apps')
    plans = request.GET.getlist('plans')
    types = request.GET.getlist('types')
    scripts = request.GET.getlist('scripts')
    status = request.GET.getlist('status')

    applications = Application.objects.filter(user=request.user)
    executions = TestExecution.objects.filter(user=request.user)
    app_scripts = ApplicationScript.objects.filter(application__in=applications)

    if status:
        executions = executions.filter(status__in=status)

    if types:
        applications = applications.filter(type__in=types)
        app_scripts = app_scripts.filter(application__in=applications)
        executions = executions.filter(script__in=app_scripts)

    if scripts:
        executions = executions.filter(script__in=scripts)

    if plans:
        executions = executions.filter(test_plan__in=plans)

    if apps:
        app_scripts = app_scripts.filter(application__in=apps)
        executions = executions.filter(script__in=app_scripts)

    all_apps = Application.objects.filter(user=request.user)
    all_strategies = TestStrategy.objects.filter(user=request.user)
    all_plans = TestPlan.objects.filter(test_strategy__in=all_strategies)
    all_types = ApplicationType.objects.all()
    all_scripts = ApplicationScript.objects.filter(application__in=all_apps)
    all_status = TestExecution.STATUS_TYPES

    context = {
        'searchParams': {
            'isSearch': len(apps) != 0 or len(plans) != 0 or len(types) != 0 or len(scripts) != 0 or len(status) != 0,
            'plans': plans,
            'apps': apps,
            'types': types,
            'scripts': scripts,
            'status': status,
        },
        'apps': all_apps,
        'plans': all_plans,
        'types': all_types,
        'scripts': all_scripts,
        'status': all_status,
        'executions': executions,
    }
    return render(request, 'TSDC/execution-detail.html', context)

