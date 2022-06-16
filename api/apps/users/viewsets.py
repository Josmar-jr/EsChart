from cgitb import text
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from .serializers import UserSerializer, ReadUserSerializer
from .models import CustomUser

@api_view(['POST', 'GET', 'PATCH', 'PUT', 'DELETE'])
def user_manager_action(request, pk=None):
    """
    FUNÇÃO RESPONSÁVEL POR REDIRECIONAR FUNCIONALIDADES PARA SEUS RESPECTIVOS MÉTODOS...
    @Author: Gilson Kedson
    @Params: request, pk
    @Date: 2022
    """
    
    if request.method == 'POST':
        return create_user(request)
    
    if request.method == 'GET':
        return read_user(pk)
    
    if request.method == 'DELETE':
        return delete_user(pk)
    
    if request.method == 'PATCH' or request.method == 'PUT':
        return update_user(request, pk)
        

def create_user(request):
    """
    FUNÇÃO RESPONSÁVEL PELA CRIAÇÃO DE USUÁRIO...
    @Author: Gilson Kedson
    @Params: request
    @Method: POST
    @Date: 2022
    """
    
    get_data = request.data
    username= get_data['username']
    email = get_data['email']
    name = get_data['name']
    password = get_data['password']
    
    password_valid = make_password(password)

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
        data.pop('password')
        user.save()
        return Response(data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_404_NOT_FOUND)


def read_user(pk=None):
    """
    FUNÇÃO RESPONSÁVEL POR PEGAR UM USUÁRIO NO BANCO DE DADOS...
    @Author: Gilson Kedson
    @Params: pk
    @Method: GET
    @Date: 2022
    """
    
    user_instance = CustomUser.objects.all().order_by('id')
    
    if pk != None:
        try:
            user = user_instance.get(id=pk)
            user_serializer = ReadUserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response("Usuário não encontrado.", status=status.HTTP_404_NOT_FOUND)
    
    users_serializer = ReadUserSerializer(user_instance, many=True)
    return Response(users_serializer.data, status=status.HTTP_200_OK)        


def delete_user(pk):
    """
    FUNÇÃO RESPONSÁVEL POR DELETAR UM USUÁRIO...
    @Author: Gilson Kedson
    @Params: pk
    @Method: DELETE
    @Date: 2022
    """
    
    try:
        user = CustomUser.objects.get(id=pk)
        user.delete()
        return Response("Usuário excluído com sucesso.", status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response("Usuário não encontrado.", status=status.HTTP_404_NOT_FOUND)


def update_user(request, pk):
    """
    FUNÇÃO RESPONSÁVEL POR ATUALIZAR DADOS DE UM USUÁRIO...
    @Author: Gilson Kedson
    @Params: request, pk
    @Method: PUT, PATCH
    @Date: 2022
    """
    
    user = CustomUser.objects.get(id=pk)
    data = request.data
    user_update = data.copy()
    
    try:    
        user_update['password'] = make_password(data['password'])
        user_serializer = UserSerializer(instance=user, data=user_update)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response("Usuário não encontrado.", status=status.HTTP_404_NOT_FOUND)