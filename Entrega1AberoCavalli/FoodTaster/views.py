from multiprocessing import context
from re import S
from ssl import HAS_TLSv1_2
from unicodedata import name
#from typing_extensions import Required
from urllib import request
from django.shortcuts import render
from FoodTaster.forms import RecipesForm
from FoodTaster.models import Dish, Recipe, Ingredient, Dish_Ingredient
from FoodTaster.forms import DishesForm, RecipesForm, IngredientForm


# Create your views here.
def index(request):
    dishes = Dish.objects.all()[:3]

    context_dict = {
        'dishes': dishes
    }

    return render(request,
                  context=context_dict,
                  template_name="FoodTaster/home.html")


def search(request):
    context_dict = dict()

    print("imprimo request: ")
    print(request)
    if request.method == 'GET':
        try:
            if request.GET['text_search']:
                search_param = request.GET['text_search']
                recipe = Recipe.objects.filter(name__contains=search_param)
        except:
            recipe = Recipe.objects.all()
        
    context_dict = {
        'recipes': recipe,
    }

    return render(
        request=request,
        context=context_dict,
        template_name="FoodTaster/searchRecipes.html",
    )


#Dishes
def dish(request, pk):
    dishes = Dish.objects.filter(pk=pk)
    #Se obtiene el la info general del plato
    #dish_info = dish.values('name', 'description')[0] 
    #Para el plato obtengo las recetas
    recipes = Recipe.objects.filter(dishCode=pk)

    context_dict = {
        'pk' : pk,
        'dishes' : dishes,
        'recipes' : recipes,
    }

    return render(
        request=request,
        context=context_dict,
        template_name="FoodTaster/dish_detail.html"
    )


def dish_list(Request):
    dishes = Dish.objects.all()

    context_dict = {
        'Dishes' : dishes,
    }

    return render(
        request=Request,
        context=context_dict,
        template_name="FoodTaster/dish_list.html")


def dish_add(Request):
    if Request.method == "POST":
        dish_form = DishesForm(Request.POST)
        if dish_form.is_valid():

            data  = dish_form.cleaned_data

            dish = Dish(name=data['name'], description=data['description'], 
            rating=data['rating'])

            dish.save()

            recipes = Recipe.objects.filter(dishCode=dish.pk)

            context_dict = {
                'dish' : dish,
                'recipes' : recipes,
            }

            return render(  request=Request, 
                            context= context_dict,
                            template_name="FoodTaster/dish_detail.html"
                        )

    form_title = "Receta"
    form_description = "Ingrese el nombre del plato de la receta, y una descripcion"
    dish_form = DishesForm(Request.POST)

    context_dict = {
        'form' : dish_form,
        'form_title' : form_title,
        'form_description' : form_description,
    }

    return render(request=Request, 
                context=context_dict,
                template_name="FoodTaster/genericForm.html"
    )


#Recipe
def recipe(Request):
    recipe = Recipe.objects.all()

    context_dict = {
        'recipe' : recipe,
    }

    return render(
       request=Request,
       context=context_dict,
       template_name="FoodTaster/recipe_list.html"
    )


def recipe_add(Request, pk=0):
    if Request.method == "POST":    
        recipe = Recipe(name=Request.POST['name'], dishCode=Request.POST['dishCode'],
            steps=Request.POST['steps'])
    
        recipe.save()

        recipes = Recipe.objects.all()

        context_dict = {
            'recipes' : recipes,
            'recipe' : recipe,
        }

        return render(
            request=Request,
            context=context_dict,
            template_name="FoodTaster/recipe_detail.html"
        )
    
    form_title = "Receta"
    form_description = "Ingrese el nombre de la Receta y su paso a paso"
    recipe_form = RecipesForm(Request.POST)

    recipe_form.dishCode = pk

    context_dict = {
        'form' : RecipesForm,
        'form_title' : form_title,
        'dish_code' : pk,
        'form_description' : form_description,
    }

    return render(request=Request, 
                context=context_dict,
                template_name="FoodTaster/recipesForm.html"
    )


#Ingredient
def ingredient(Request):
    ingredient = Ingredient.objects.all()

    context_dict = {
        'ingredients' : ingredient,
    }

    return render(
       request=Request,
       context=context_dict,
       template_name="FoodTaster/ingredient_list.html"
    )

def ingredient_add(Request):
    if Request.method == "POST":
        ingredient = Ingredient(name=Request.POST['name'], 
        description=Request.POST['description'])
    
        ingredient.save()

        context_dict = {
            'ingredient' : ingredient,
        }

        return render(
            request=Request,
            context=context_dict,
            template_name="FoodTaster/ingredient_detail.html"
        )
    
    form_title = "ingrediente"
    form_description = "Ingrese el nombre del ingrediente"
    ingredient_form = IngredientForm(Request.POST)

    context_dict = {
        'form' : IngredientForm,
        'form_title' : form_title,
        'form_description' : form_description,
    }

    return render(request=Request, 
                context=context_dict,
                template_name="FoodTaster/genericForm.html"
    )
