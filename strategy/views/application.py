# coding=utf-8
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from strategy.models.application import Application
from strategy.forms.application import ApplicationForm


@method_decorator(login_required(), name='dispatch')
class ApplicationCreate(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'forms/application-form.html'
    success_url = reverse_lazy('application-list')


@method_decorator(login_required(), name='dispatch')
class ApplicationList(ListView):
    model = Application
    template_name = 'TSDC/application-list.html'
    paginate_by = 20


@method_decorator(login_required(), name='dispatch')
class ApplicationEdit(UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'forms/application-form.html'
    success_url = reverse_lazy('application-list')


@method_decorator(login_required(), name='dispatch')
class ApplicationDetail(DetailView):
    model = Application
    template_name = 'TSDC/application-detail.html'


@method_decorator(login_required(), name='dispatch')
class ApplicationDelete(DeleteView):
    model = Application
    template_name = 'confirmation/delete-application.html'
    success_url = reverse_lazy('application-list')
