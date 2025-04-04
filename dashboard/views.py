from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView
from core.models import Recipe


class DashboardDetailView(LoginRequiredMixin, DetailView):
    http_method_names = ["get"]
    template_name = "dashboard/detail.html"
    model = User
    context_object_name = "recipes"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["recipes"] = Recipe.objects.filter(author=user)
        return context