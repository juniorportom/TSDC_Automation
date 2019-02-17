from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormFull(UserCreationForm):
    email = forms.EmailField(required=True, help_text='El correo es requerido.')
    first_name = forms.Field(required=True, help_text='El nombre es requerido.')
    last_name = forms.Field(required=True, help_text='El apellido es requerido.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya está en uso.')
        return email
