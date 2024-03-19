from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wine.php", views.wine, name="wine")
]
