from django.urls import path, include
from . import views as base_views

urlpatterns = [
    path('masters/cities/', base_views.get_cities)
]