from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', )