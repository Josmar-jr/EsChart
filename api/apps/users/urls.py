from venv import create
from django.urls import path
from . import viewsets

urlpatterns = [
    path('create-user', viewsets.create_user, name='create-user'),
]