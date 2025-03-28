from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=240)
    ingredients = models.CharField(max_length=400)
    instructions = models.CharField(max_length=400)

    def __str__(self):
        return self.name[0:100]