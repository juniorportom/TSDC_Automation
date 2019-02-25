# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.testStrategy import TestStrategy

"""
Formulario para una estrategia de pruebas
"""


class TestStrategyForm(forms.ModelForm):
    class Meta:
        model = TestStrategy
        fields = ['name', 'test_level', 'objective', 'application_version']
        labels = {
            'name': _("Nombre"),
            'test_level': _("Nivel de Pruebas"),
            'objective': _("Objetivo"),
            'application_version': _("Aplicación"),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'test_level': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nivel de Pruebas'}),
            'objective': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Objetivo'}),
            'application_version': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Aplicación'})
        }

