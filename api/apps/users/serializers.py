from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'password')