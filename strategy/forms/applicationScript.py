# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.applicationScript import ApplicationScript

"""
Formulario para registro de un plan de pruebas
"""


class ApplicationScriptForm(forms.ModelForm):
    class Meta:
        model = ApplicationScript
        fields = ['name', 'script_file', 'technique_test']
        labels = {
            'name': _("Nombre"),
            'script_file': _("Script"),
            'technique_test': _("Técnica de pruebas")
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'script_file': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'placeholder': 'Script'}),
            'technique_test': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Técnica de pruebas'})
        }
