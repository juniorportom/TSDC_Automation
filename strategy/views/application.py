# coding=utf-8
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from strategy.models.application import Application
from strategy.forms.application import ApplicationForm


class ApplicationCreate(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'forms/application-form.html'
    success_url = reverse_lazy('home')