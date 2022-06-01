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

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name=models.CharField(max_length=100)
    dishCode=models.IntegerField()
    ingredientCode=models.IntegerField()
    ingredientAmount=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'