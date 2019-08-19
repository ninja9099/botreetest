

from django.urls import path
from . import views as user_views

urlpatterns = [
    path('cleaner/manage/', user_views.manage_cleaner)
]