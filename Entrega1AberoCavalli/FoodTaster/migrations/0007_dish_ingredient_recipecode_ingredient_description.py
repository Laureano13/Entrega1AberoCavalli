# Generated by Django 4.0.4 on 2022-06-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTaster', '0006_alter_recipe_dishcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish_ingredient',
            name='recipeCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]