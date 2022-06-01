from optparse import Values
import re
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DishesForm(forms.Form):
    name=forms.CharField(label="Nombre del Plato", max_length=60, required=True)
    description=forms.CharField(label="Descripcion",max_length=200, min_length=10, required=True)
    rating=forms.FloatField(label="Dale un puntaje del 1 al 10", max_value=10, min_value=1, required=False)


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

