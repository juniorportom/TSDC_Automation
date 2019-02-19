# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.application import Application

"""
Formulario para una applicacion
"""


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'type', 'description', 'architecture', 'developer_stack']
        labels = {
            'name': _("Nombre"),
            'type': _("Tipo"),
            'description': _("Descripción"),
            'architecture': _("Arquitectura"),
            'developer_stack': _("Desarrollada en"),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'architecture': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Arquitectura'}),
            'developer_stack': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Desarrollada en:'})
        }

