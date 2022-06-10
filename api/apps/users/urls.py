from venv import create
from django.urls import path
from . import viewsets

urlpatterns = [
    path('create-user', viewsets.create_user, name='create-user'),
    path('read-user/', viewsets.read_user, name='read-user'),
    path('read-user/<int:pk>', viewsets.read_user, name='read-user'),
    path('update-user/<int:pk>', viewsets.update_user, name='update-user'),
    path('delete-user/<int:pk>', viewsets.delete_user, name='delete-user'),
]