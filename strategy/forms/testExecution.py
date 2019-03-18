# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.testExecution import TestExecution

"""
Formulario para registro de un plan de pruebas
"""


class TestExecutionForm(forms.ModelForm):
    class Meta:
        model = TestExecution
        fields = ['test_plan', 'iteration', 'status', 'execution_date', 'browser', 'mobile_so', 'script']
