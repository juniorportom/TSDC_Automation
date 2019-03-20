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

    applications = Application.objects.all()
    executions = TestExecution.objects.all()
    app_scripts = ApplicationScript.objects.all()
    test_plans = TestPlan.objects.all()
    app_types = ApplicationType.objects.all()

    sts = []
    for st in status:
        sts.append(st)
        executions = executions.filter(status__in=sts)

    for pk in types:
        app_types = app_types.filter(id__in=pk)
        applications = applications.filter(type__in=app_types)
        app_scripts = app_scripts.filter(application__in=applications)
        executions = executions.filter(script__in=app_scripts)

    for pk in scripts:
        app_scripts = app_scripts.filter(id__in=pk)
        executions = executions.filter(script__in=app_scripts)

    for pk in plans:
        test_plans = test_plans.filter(id__in=pk)
        executions = executions.filter(test_plan__in=test_plans)

    for pk in apps:
        applications = applications.filter(id=pk)
        app_scripts = app_scripts.filter(application__in=applications)
        executions = executions.filter(script__in=app_scripts)

    all_apps = Application.objects.all()
    all_plans = TestPlan.objects.all()
    all_types = ApplicationType.objects.all()
    all_scripts = ApplicationScript.objects.all()
    all_status = TestExecution.STATUS_TYPES

    context = {
        'searchParams': {
            'isSearch': len(apps) != 0 or len(plans) !=0,
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

