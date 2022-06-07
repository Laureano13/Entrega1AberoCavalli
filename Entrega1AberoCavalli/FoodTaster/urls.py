from django.urls import path
from FoodTaster import views

app_name='FoodTaster'
urlpatterns = [
    path('', views.index, name='home'),
    
    path('dishes', views.dish_list, name='dish-list'),
    path('dish/<int:pk>', views.dish, name='dish-detail'),
    path('dish/add', views.dish_add, name='dish-add'),

    path('recipes', views.recipe, name='recipe-list'),
    path('recipe/add/<int:pk>', views.recipe_add, name='recipe-add'),

    path('ingredient', views.ingredient, name='ingredient-list'),
    path('ingredient/add', views.ingredient_add, name='ingredient-add'),

    path('search-recipes', views.search, name='search-recipe'),
]