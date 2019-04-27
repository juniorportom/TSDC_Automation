# coding=utf-8
from django.shortcuts import render
import json
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
import requests


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
    steps = request.GET.getlist('steps')
    exec_id = request.GET.get('exec')
    all_steps = StepImage.objects.filter(test_execution_id=exec_id).order_by('id')

    context = {
        'searchParams': {
            'isSearch': len(steps) != 0,
            'steps': steps
        },
        'steps': all_steps
    }
    return render(request, 'TSDC/step_dropdown_list_options.html', context)


def load_steps2(request):
    steps = request.GET.getlist('steps2')
    exec_id = request.GET.get('exec2')
    all_steps = StepImage.objects.filter(test_execution_id=exec_id).order_by('id')

    context = {
        'searchParams': {
            'isSearch': len(steps) != 0,
            'steps2': steps
        },
        'steps2': all_steps
    }
    return render(request, 'TSDC/step_dropdown_list_options2.html', context)


def load_imgs(request):
    steps = json.loads(request.GET.get('steps_list'))

    if steps:
        steps_part1 = StepImage.objects.filter(id__in=steps)

    context = {
        'stepsImgs': steps_part1
    }
    return render(request, 'TSDC/step_img_list.html', context)


def load_imgs2(request):
    steps = json.loads(request.GET.get('steps_list2'))

    if steps:
        steps_part2 = StepImage.objects.filter(id__in=steps)

    context = {
        'stepsImgs2': steps_part2
    }
    return render(request, 'TSDC/step_img_list2.html', context)


def load_diffs(request):
    steps1 = json.loads(request.GET.get('steps_list1'))
    steps2 = json.loads(request.GET.get('steps_list2'))


    imgs_diffs = []

    if steps1 and steps2 and len(steps1) == len(steps2):
        if steps1:
            steps_part1 = StepImage.objects.filter(id__in=steps1)

        if steps2:
            steps_part2 = StepImage.objects.filter(id__in=steps2)

        for i in range(len(steps_part1)):
            response =  requests.post('http://localhost:8080/compare-images',
                data={'image1': steps_part1[i].get_absolute_s3_img_url(),
                    'image2': steps_part2[i].get_absolute_s3_img_url(),
                    'idImg1': steps_part1[i].id,
                    'idImg2':steps_part2[i].id,
                      'idExec1': steps_part1[i].test_execution.id,
                      'idExec2': steps_part2[i].test_execution.id,
                      }).json()
            vrt = VRTElem(response['report']['idImg1'], response['report']['idImg2'], response['report']['imageDiff'])
            print(response['report']['imageDiff'])
            imgs_diffs.append(vrt)

    context = {
        'diffs': imgs_diffs
    }

    return render(request, 'TSDC/step_img_diff.html', context)


class VRTElem:
    def __init__(self, id1, id2, img):
        self.id1 = id1
        self.id2 = id2
        self.img = img
