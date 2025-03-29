from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("<int:pk>/", views.RecipeDetailView.as_view(), name="detail"),
    path("new/", views.CreateNewRecipe.as_view(), name="new_recipe"),
]