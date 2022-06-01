from django.contrib import admin

# Register your models here.
from FoodTaster.models import Dish, Ingredient, Recipe

admin.site.register(Dish)

admin.site.register(Ingredient)

admin.site.register(Recipe)