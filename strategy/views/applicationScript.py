# coding=utf-8
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from strategy.models.applicationScript import ApplicationScript
from strategy.models.application import Application
from strategy.forms.applicationScript import ApplicationScriptForm


@method_decorator(login_required(), name='dispatch')
class ApplicationScriptCreate(CreateView):
    model = ApplicationScript
    form_class = ApplicationScriptForm
    template_name = 'forms/application-script-form.html'

    def form_valid(self, form):
        form.instance.application = get_object_or_404(Application, id=self.kwargs['application_id'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail-application', kwargs={'pk': self.kwargs['application_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application_id'] = self.kwargs['application_id']
        return context


@method_decorator(login_required(), name='dispatch')
class ApplicationScriptEdit(UpdateView):
    model = ApplicationScript
    form_class = ApplicationScriptForm
    template_name = 'forms/application-script-form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail-application', kwargs={'pk': self.kwargs['application_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application_id'] = self.kwargs['application_id']
        return context


@method_decorator(login_required(), name='dispatch')
class ApplicationScriptDelete(DeleteView):
    model = ApplicationScript
    template_name = 'confirmation/delete-application-script.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail-application', kwargs={'pk': self.kwargs['application_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application_id'] = self.kwargs['application_id']
        return context
