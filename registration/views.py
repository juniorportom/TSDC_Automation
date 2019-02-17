from .forms import UserCreationFormFull
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.

class SingUpView(CreateView):
    form_class = UserCreationFormFull
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Correo electronico'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Repetir contraseña'})
        return form
