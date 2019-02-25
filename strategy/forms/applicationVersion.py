# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.applicationVersion import ApplicationVersion

"""
Formulario para una version de applicacion
"""


class ApplicationVersionForm(forms.ModelForm):
    class Meta:
        model = ApplicationVersion
        fields = ['version', 'url_repository']
        labels = {
            'version': _(" Versión"),
            'url_repository': _("URL Repositorio")
        }
        widgets = {
            'version': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Versión'}),
            'url_repository': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL Repositorio'})
        }

