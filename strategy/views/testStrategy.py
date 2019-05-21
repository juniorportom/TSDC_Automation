# coding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from strategy.models.testPlan import TestPlan
from strategy.models.testStrategy import TestStrategy
from strategy.models.applicationVersion import ApplicationVersion
from strategy.models.application import Application
from strategy.forms.testStrategy import TestStrategyForm


@method_decorator(login_required(), name='dispatch')
class TestStrategyCreate(CreateView):
    model = TestStrategy
    form_class = TestStrategyForm
    template_name = 'forms/test-strategy-form.html'
    success_url = reverse_lazy('test-strategy-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required(), name='dispatch')
class TestStrategyList(ListView):
    model = TestStrategy
    template_name = 'TSDC/test-strategy-list.html'
    paginate_by = 20

    def get_queryset(self):
        object_list = self.model.objects.filter(user=self.request.user)
        return object_list


@method_decorator(login_required(), name='dispatch')
class TestStrategyEdit(UpdateView):
    model = TestStrategy
    form_class = TestStrategyForm
    template_name = 'forms/test-strategy-form.html'
    success_url = reverse_lazy('test-strategy-list')


@method_decorator(login_required(), name='dispatch')
class TestStrategyDetail(DetailView):
    model = TestStrategy
    context_object_name = 'strategy'
    template_name = 'TSDC/test-strategy-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = TestPlan.objects.filter(test_strategy=self.object)
        version = get_object_or_404(ApplicationVersion, id=self.object.application_version.id)
        context['application'] = get_object_or_404(Application, id=version.application.id)
        return context


@method_decorator(login_required(), name='dispatch')
class TestStrategyDelete(DeleteView):
    model = TestStrategy
    template_name = 'confirmation/delete-test-strategy.html'
    success_url = reverse_lazy('test-strategy-list')