# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.testPlan import TestPlan

"""
Formulario para registro de un plan de pruebas
"""


class TestPlanForm(forms.ModelForm):
    class Meta:
        model = TestPlan
        fields = ['description', 'technique_test', 'browser', 'mobile_so', 'script_file', 'execution_date', 'iterations']
        labels = {
            'description': _("Descripción"),
            'technique_test': _("Técnica de pruebas"),
            'browser': _("Navegador"),
            'mobile_so': _("Mobile SO"),
            'script_file': _("Script"),
            'execution_date': _("Fecha de ejecución"),
            'iterations': _("Iteraciones"),
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'technique_test': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Técnica de pruebas'}),
            'browser': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Navegador'}),
            'mobile_so': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Mobile SO'}),
            'script_file': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Script'}),
            'execution_date': forms.DateTimeInput(format=('%Y-%m-%d %H:%M'), attrs={'class': 'form-control','placeholder':'yyyy-MM-dd HH:MM', 'type': 'datetime'}),
            'iterations': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Iteraciones'}),
        }
