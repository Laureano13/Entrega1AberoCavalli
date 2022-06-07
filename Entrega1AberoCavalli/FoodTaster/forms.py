from optparse import Values
from pydoc import describe
import re
from unicodedata import name
from django import forms
from django.forms import ModelForm
from FoodTaster.models import Recipe, Dish, Ingredient

class DishesForm(forms.Form):
    name=forms.CharField(label="Nombre del Plato", max_length=60, required=True)
    description=forms.CharField(label="Descripcion",max_length=200, min_length=10, required=True)
    rating=forms.FloatField(label="Dale un puntaje del 1 al 10", max_value=10, min_value=1, required=False)


class RecipesForm(forms.Form):
    name=forms.CharField(label="Nombre", max_length=100, required=True)
    dishCode=forms.ModelChoiceField(queryset=Dish.objects.all().order_by('pk'), required=True)
    steps=forms.CharField(label="Receta", max_length=400, required=True)


class IngredientForm(forms.Form):
    name=forms.CharField(label="Nombre", max_length=100, required=True)
    description=forms.CharField(label="Description", max_length=200, required=False)