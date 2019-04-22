# coding=utf-8
from django import forms
from django.utils.translation import gettext as _
from strategy.models.vrtTest import VrtTest

"""
Formulario para registro de un plan de pruebas
"""


class ApplicationScriptForm(forms.ModelForm):
    class Meta:
        model = VrtTest
        fields = ['step_image_a', 'step_image_b', 'image_diff']
        labels = {
            'step_image_a': _("Imagen 1"),
            'step_image_b': _("Imagen 2"),
            'image_diff': _("Imagen con diferencias")
        }
        widgets = {
            'step_image_a': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Imagen 1'}),
            'step_image_b': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Imagen 2'}),
            'image_diff': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'placeholder': 'Imagen con diferencias'})
        }