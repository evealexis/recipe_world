from django.views.generic import ListView

from .models import Recipe

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "core/home.html"
    model = Recipe
    context_object_name = "recipes"
    queryset = Recipe.objects.all().order_by('-id')[0:30]