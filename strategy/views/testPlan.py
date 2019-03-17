# coding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from strategy.models.testPlan import TestPlan
from strategy.models.testStrategy import TestStrategy
from strategy.models.applicationScript import ApplicationScript

from strategy.forms.testPlan import TestPlanForm
from strategy.models.applicationVersion import ApplicationVersion
from strategy.models.application import Application


@method_decorator(login_required(), name='dispatch')
class TestPlanCreate(CreateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = 'forms/test-plan-form.html'

    def form_valid(self, form):
        form.instance.test_strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail-test-strategy', kwargs={'pk': self.kwargs['strategy_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strategy_id'] = self.kwargs['strategy_id']
        context['strategy'] = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        version = get_object_or_404(ApplicationVersion, id=strategy.application_version.id)
        context['application'] = get_object_or_404(Application, id=version.application.id)
        #app = get_object_or_404(Application, id=version.application.id)
        #context['scripts'] = ApplicationScript.objects.filter(application=app)
        #context['scripts'] = TestPlanForm.ModelChoiceField(queryset=SkillsReference.objects.filter(person=self.person)
        #self.fields['scripts'].queryset = ApplicationScript.objects.all()
        return context


@method_decorator(login_required(), name='dispatch')
class TestPlanEdit(UpdateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = 'forms/test-plan-form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail-test-strategy', kwargs={'pk': self.kwargs['strategy_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strategy_id'] = self.kwargs['strategy_id']
        context['strategy'] = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        version = get_object_or_404(ApplicationVersion, id=strategy.application_version.id)
        context['application'] = get_object_or_404(Application, id=version.application.id)
        return context


@method_decorator(login_required(), name='dispatch')
class TestPlanDelete(DeleteView):
    model = TestPlan
    template_name = 'confirmation/delete-test-plan.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail-test-strategy', kwargs={'pk': self.kwargs['strategy_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strategy_id'] = self.kwargs['strategy_id']
        return context
