from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("<str:username>/", views.DashboardDetailView.as_view(), name="detail"),
]