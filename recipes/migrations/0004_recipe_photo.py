# Generated by Django 4.1.3 on 2023-01-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_body_remove_recipe_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='pics'),
        ),
    ]
