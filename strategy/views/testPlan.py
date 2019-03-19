# coding=utf-8
import boto3
from django.conf import settings
import os
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from strategy.models.testPlan import TestPlan
from strategy.models.testStrategy import TestStrategy
from strategy.forms.testPlan import TestPlanForm
from strategy.models.applicationVersion import ApplicationVersion
from strategy.models.application import Application
from strategy.models.testExecution import TestExecution


@method_decorator(login_required(), name='dispatch')
class TestPlanCreate(CreateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = 'forms/test-plan-form.html'

    def get_form_kwargs(self):
        kwargs = super(TestPlanCreate, self).get_form_kwargs()
        kwargs['strategy_id'] = self.kwargs['strategy_id']
        return kwargs

    def form_valid(self, form):
        form.instance.test_strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        if not form.instance.execute_immediately:
            form.instance.status = 'R'
        else:
            form.instance.status = 'P'

        self.object = form.save()
        testPlan = get_object_or_404(TestPlan, id=self.object.id)

        if testPlan.execute_immediately:

            strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
            version = get_object_or_404(ApplicationVersion, id=strategy.application_version.id)
            app = get_object_or_404(Application, id=version.application.id)

            if app.type.name == 'Mobile':
                for mobile in testPlan.mobile_list():
                    for script in testPlan.script_list():
                        for iteration in range(testPlan.iterations):
                            execution = TestExecution()
                            execution.test_plan = testPlan
                            execution.iteration = iteration + 1
                            execution.status = 'P'
                            execution.mobile_so = mobile
                            execution.execution_date = testPlan.execution_date
                            execution.script = script
                            execution.user = self.request.user
                            execution.save()
                            last_exec = TestExecution.objects.latest('id')

                            sqs = boto3.client('sqs',
                                               aws_access_key_id=settings.AWS_ACCESS_KEY_ID_SQS,
                                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY_SQS,
                                               region_name='us-east-2')
                            queue_url = os.environ["URL_SQS"]
                            response = sqs.send_message(
                                QueueUrl=queue_url,
                                MessageAttributes={
                                },
                                MessageBody=(
                                    "app.send_task('" + script.technique_test.function_name + "', kwargs={'arg1': " + str(last_exec.id) + "})"
                                ),
                                MessageGroupId="MessageGroupId" + str(last_exec.id)
                            )
            else:
                for browser in testPlan.browser_list():
                    for script in testPlan.script_list():
                        for iteration in range(testPlan.iterations):
                            execution = TestExecution()
                            execution.test_plan = testPlan
                            execution.iteration = iteration + 1
                            execution.status = 'P'
                            execution.browser = browser
                            execution.execution_date = testPlan.execution_date
                            execution.script = script
                            execution.user = self.request.user
                            execution.save()
                            last_exec = TestExecution.objects.latest('id')

                            sqs = boto3.client('sqs',
                                               aws_access_key_id=settings.AWS_ACCESS_KEY_ID_SQS,
                                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY_SQS,
                                               region_name='us-east-2')
                            queue_url = os.environ["URL_SQS"]
                            response = sqs.send_message(
                                QueueUrl=queue_url,
                                MessageAttributes={
                                },
                                MessageBody=(
                                        "app.send_task('" + script.technique_test.function_name + "', kwargs={'arg1': " + str(last_exec.id) + "})"
                                ),
                                MessageGroupId="MessageGroupId" + str(last_exec.id)
                            )

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
        return context


@method_decorator(login_required(), name='dispatch')
class TestPlanEdit(UpdateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = 'forms/test-plan-form.html'

    def get_success_url(self, **kwargs):

        testPlan = get_object_or_404(TestPlan, id=self.object.id)

        if testPlan.execute_immediately:

            strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
            version = get_object_or_404(ApplicationVersion, id=strategy.application_version.id)
            app = get_object_or_404(Application, id=version.application.id)

            if app.type.name == 'Mobile':
                for mobile in testPlan.mobile_list():
                    for script in testPlan.script_list():
                        for iteration in range(testPlan.iterations):
                            execution = TestExecution()
                            execution.test_plan = testPlan
                            execution.iteration = iteration + 1
                            execution.status = 'P'
                            execution.mobile_so = mobile
                            execution.execution_date = testPlan.execution_date
                            execution.script = script
                            execution.user = self.request.user
                            execution.save()
                            last_exec = TestExecution.objects.latest('id')

                            sqs = boto3.client('sqs',
                                               aws_access_key_id=settings.AWS_ACCESS_KEY_ID_SQS,
                                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY_SQS,
                                               region_name='us-east-2')
                            queue_url = os.environ["URL_SQS"]
                            response = sqs.send_message(
                                QueueUrl=queue_url,
                                MessageAttributes={
                                },
                                MessageBody=(
                                        "app.send_task('" + script.technique_test.function_name + "', kwargs={'arg1': " + str(last_exec.id) + "})"
                                ),
                                MessageGroupId="MessageGroupId" + str(last_exec.id)
                            )
            else:
                for browser in testPlan.browser_list():
                    for script in testPlan.script_list():
                        for iteration in range(testPlan.iterations):
                            execution = TestExecution()
                            execution.test_plan = testPlan
                            execution.iteration = iteration + 1
                            execution.status = 'P'
                            execution.browser = browser
                            execution.execution_date = testPlan.execution_date
                            execution.script = script
                            execution.user = self.request.user
                            execution.save()
                            last_exec = TestExecution.objects.latest('id')

                            sqs = boto3.client('sqs',
                                               aws_access_key_id=settings.AWS_ACCESS_KEY_ID_SQS,
                                               aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY_SQS,
                                               region_name='us-east-2')
                            queue_url = os.environ["URL_SQS"]
                            response = sqs.send_message(
                                QueueUrl=queue_url,
                                MessageAttributes={
                                },
                                MessageBody=(
                                        "app.send_task('" + script.technique_test.function_name + "', kwargs={'arg1': " + str(last_exec.id) + "})"
                                ),
                                MessageGroupId="MessageGroupId" + str(last_exec.id)
                            )

        return reverse_lazy('detail-test-strategy', kwargs={'pk': self.kwargs['strategy_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['strategy_id'] = self.kwargs['strategy_id']
        context['strategy'] = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        strategy = get_object_or_404(TestStrategy, id=self.kwargs['strategy_id'])
        version = get_object_or_404(ApplicationVersion, id=strategy.application_version.id)
        context['application'] = get_object_or_404(Application, id=version.application.id)
        return context

    def form_valid(self, form):
        if not form.instance.execute_immediately:
            form.instance.status = 'R'
        else:
            form.instance.status = 'P'

        return super().form_valid(form)


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
