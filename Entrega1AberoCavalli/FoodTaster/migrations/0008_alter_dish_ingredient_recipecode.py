# Generated by Django 4.0.4 on 2022-06-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTaster', '0007_dish_ingredient_recipecode_ingredient_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish_ingredient',
            name='recipeCode',
            field=models.IntegerField(),
        ),
    ]
