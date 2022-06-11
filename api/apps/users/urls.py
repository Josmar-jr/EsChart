from venv import create
from django.urls import path
from . import viewsets

urlpatterns = [
    path('user', viewsets.user_manager_action),
    path('user/<int:pk>', viewsets.user_manager_action)
]