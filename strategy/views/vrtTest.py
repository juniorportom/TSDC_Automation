# coding=utf-8
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

from strategy.models.testExecution import TestExecution
from strategy.forms.testExecution import TestExecutionForm
from strategy.models.application import Application
from strategy.models.applicationScript import ApplicationScript
from strategy.models.stepImage import StepImage
from strategy.models.testPlan import TestPlan
from strategy.models.applicationType import ApplicationType
from strategy.models.testStrategy import TestStrategy
from strategy.views.sqsMessage import send_message
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def applications_vrt(request):
    app = request.GET.get('apps', -1)
    app = int(app)

    all_apps = Application.objects.filter(user=request.user)

    context = {
        'searchParams': {
            'isSearch': app != -1,
            'app': app
        },
        'apps': all_apps
    }
    return render(request, 'TSDC/vrt-test.html', context)


def load_scripts(request):
    script = request.GET.get('scripts', -1)
    script = int(script)
    app_id = request.GET.get('app')
    all_scripts = ApplicationScript.objects.filter(application__in=app_id).order_by('name')

    context = {
        'searchParams': {
            'isSearch': script != -1,
            'script': script
        },
        'scripts': all_scripts
    }
    return render(request, 'TSDC/script_dropdown_list_options.html', context)


def load_execs(request):
    exc = request.GET.get('execs', -1)
    exc = int(exc)
    script_id = request.GET.get('script')
    all_execs = TestExecution.objects.filter(script__in=script_id).filter(status='S').order_by('id')

    context = {
        'searchParams': {
            'isSearch': exc != -1,
            'exec': exc
        },
        'execs': all_execs
    }
    return render(request, 'TSDC/exec_dropdown_list_options.html', context)


def load_steps(request):
    step = request.GET.get('step', -1)
    step = int(step)
    exec_id = request.GET.get('exec')
    print('Exec: ' + str(exec_id))
    all_steps = StepImage.objects.filter(test_execution__in=exec_id).order_by('id')

    context = {
        'searchParams': {
            'isSearch': step != -1,
            'step': step
        },
        'steps': all_steps
    }
    return render(request, 'TSDC/step_dropdown_list_options.html', context)