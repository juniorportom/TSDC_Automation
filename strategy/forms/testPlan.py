# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.testPlan import TestPlan
from django.shortcuts import get_object_or_404


from strategy.models.testStrategy import TestStrategy

from strategy.models.applicationScript import ApplicationScript


from strategy.models.applicationVersion import ApplicationVersion
from strategy.models.application import Application


"""
Formulario para registro de un plan de pruebas
"""


class TestPlanForm(forms.ModelForm):
    class Meta:
        model = TestPlan
        fields = ('description', 'iterations', 'browser', 'mobile_so', 'scripts', 'execute_immediately', 'execution_date')

        labels = {
            'description': _("Descripción"),
            'iterations': _("Iteraciones"),
            'browser': _("Navegadores"),
            'mobile_so': _("Movíles"),
            'scripts': _("Scripts de pruebas"),
            'execute_immediately': _("Ejecutar inmediatamente"),
            'execution_date': _("Fecha de ejecución"),

        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'iterations': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Iteraciones'}),
            'browser': forms.CheckboxSelectMultiple(attrs={'class': '', 'placeholder': 'Navegadores'}),
            'mobile_so': forms.CheckboxSelectMultiple(attrs={'class': '', 'placeholder': 'Movíles'}),
            'scripts': forms.CheckboxSelectMultiple(attrs={'class': '', 'placeholder': 'Scripts de pruebas'}),
            'execute_immediately': forms.CheckboxInput(attrs={'class': '', 'placeholder': 'Ejecutar inmediatamente'}),
            'execution_date': forms.DateTimeInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd HH:MM', 'type': 'datetime'}),
            # 'scripts': forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=list(ApplicationScript.objects.all())),
        }

        def __init__(self, *args, **kwargs):
            strategy_id = kwargs.pop['strategy_id']  # kwargs.pop('application')
            super(TestPlanForm, self).__init__(*args, **kwargs)
            print('Esta es la estrategia:')
            strategy = get_object_or_404(TestStrategy, id=strategy_id)
            version = get_object_or_404(ApplicationVersion, id=strategy.application_version.id)
            application = get_object_or_404(Application, id=version.application.id)
            self.fields['scripts'].queryset = ApplicationScript.objects.filter(application=application)





