from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from django.contrib.auth.hashers import make_password

from .serializers import UserSerializer, ReadUserSerializer
from .models import CustomUser

@api_view(['POST', 'GET', 'PATCH', 'PUT', 'DELETE'])
def user_manager_action(request, pk=None):
    if request.method == 'POST':
        return create_user(request)
    
    if request.method == 'GET':
        return read_user(request, pk)
    
    if request.method == 'PATCH' or request.method == 'PUT':
        return update_user(request, pk)
        
    if request.method == 'DELETE':
        return delete_user(request, pk)

def create_user(request):
    username= request.data['username']
    email = request.data['email']
    name = request.data['name']
    password = request.data['password']
    password_valid = make_password(password)
    context_response = {}

    data = {
        'username': username,
        'email': email,
        'name': name,
        'password': password_valid
    }

    user = UserSerializer(data=data)
    user_instance = CustomUser.objects.all()

    if user_instance.filter(username=data['username']).exists():
        raise serializers.ValidationError("Usuário com esse login já existe, tente outro!")

    if user_instance.filter(email=data['email']).exists():
        raise serializers.ValidationError("Usuário com esse email já existe, tente outro!")

    if user.is_valid():
        context_response['name'] = request.data['name']
        context_response['username'] = request.data['username']
        context_response['email'] = request.data['email']
        user.save()

        return Response(context_response, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_404_NOT_FOUND)

def read_user(request, pk=None):    
    user_instance = CustomUser.objects.all()
    
    if pk != None:
        try:
            user = user_instance.get(id=pk)
            user_serializer = ReadUserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response("Usuário não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
    users_serializer = ReadUserSerializer(user_instance, many=True)
    return Response(users_serializer.data, status=status.HTTP_200_OK)        

def delete_user(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)
        user.delete()
        return Response("Usuário excluído com sucesso.", status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response("Usuário não encontrado.", status=status.HTTP_404_NOT_FOUND)

def update_user(request):
    pass