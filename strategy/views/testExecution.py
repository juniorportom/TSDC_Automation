# coding=utf-8
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from strategy.models.testExecution import TestExecution


@method_decorator(login_required(), name='dispatch')
class TestExecutionList(ListView):
    model = TestExecution
    template_name = 'TSDC/execution-detail.html'
    paginate_by = 20
    context_object_name = 'executions'

    def get_queryset(self):
        object_list = self.model.objects.filter(user=self.request.user)
        return object_list


