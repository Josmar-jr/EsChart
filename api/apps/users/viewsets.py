from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from .models import CustomUser


# Create your views here.
@api_view(['POST'])
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

    if user_instance.filter(username=request.data['username']).exists():
        raise serializers.ValidationError("Usuário com esse login já existe, tente outro!")

    if user_instance.filter(username=request.data['email']).exists():
        raise serializers.ValidationError("Usuário com esse email já existe, tente outro!")

    if user.is_valid():
        user.save()

        context_response['name'] = request.data['name']
        context_response['username'] = request.data['username']
        context_response['email'] = request.data['email']

        return Response(context_response, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def read_user(request, pk=None):
    pass

@api_view(['PUT', 'PATCH'])
def update_user(request):
    pass

@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)
        user.delete()
        return Response("Usuário excluído com sucesso.", status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response("Usuário não encontrado.", status=status.HTTP_404_NOT_FOUND)