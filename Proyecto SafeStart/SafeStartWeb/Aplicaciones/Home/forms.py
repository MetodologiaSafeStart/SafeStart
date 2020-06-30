from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Usuario

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class Perfil(forms.ModelForm):   
   user=forms.CharField(widget=forms.HiddenInput())
   class Meta:
        model = Usuario
        fields =('fecha_nacimiento','foto_perfil','profesion','presentacion','enlace_referencias',)