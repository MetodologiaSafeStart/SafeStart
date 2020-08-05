from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Usuario, Proyecto

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

   user=forms.CharField(max_length=140, required=True)

   user=forms.CharField(max_length=140, required=True)#widget=forms.HiddenInput()

   class Meta:
        model = Usuario
        fields =('fecha_nacimiento','foto_perfil','profesion','presentacion','enlace_referencias',)

class Proyecto(forms.ModelForm):   

   user=forms.CharField(max_length=140, required=True)

   user=forms.CharField(max_length=140, required=True)#widget=forms.HiddenInput()

   class Meta:
        model = Proyecto
        fields =('nombre_proyecto','descripcion_proyecto',
	'foto_proyecto','foto_proyecto2',
	'nombre_usuario','rubro',)