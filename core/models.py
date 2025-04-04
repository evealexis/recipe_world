from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField


class Recipe(models.Model):
    name = models.CharField(max_length=240)
    ingredients = models.CharField(max_length=400)
    instructions = models.CharField(max_length=400)
    image = ImageField(upload_to="media/")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.name[0:100]
