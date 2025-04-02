from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "core/home.html"
    model = Recipe
    context_object_name = "recipes"
    queryset = Recipe.objects.all().order_by('-id')[0:30]


class RecipeDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "core/detail.html"
    model = Recipe
    context_object_name = "recipe"


class CreateNewRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "core/create.html"
    fields = ['name', 'ingredients', 'instructions', 'image']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)