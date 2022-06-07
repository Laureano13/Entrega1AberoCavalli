from django.db import models

# Create your models here.
class Dish(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    rating=models.FloatField()

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}'


class Dish_Ingredient(models.Model):
    dishCode=models.IntegerField(default=0)
    recipeCode=models.IntegerField(default=0)
    ingredientCode=models.IntegerField(default=0)
    ingredientAmount=models.CharField(max_length=100)

    def __str__(self):
        return ''


class Recipe(models.Model):
    name=models.CharField(max_length=100, null=True)
    dishCode=models.IntegerField(null=True)
    steps=models.CharField(max_length=400, null=True)

    def __str__(self):
        return f'{self.name}'

    def desc(self):
        return f'{self.description}'