# Generated by Django 4.0.4 on 2022-06-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTaster', '0003_dish_ingredient_remove_recipe_ingredientamount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
