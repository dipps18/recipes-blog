from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    steps = models.TextField(default="")
    ingredients = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='pics', default="pics/default.jpg")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])
