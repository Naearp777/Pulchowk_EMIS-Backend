from rest_framework import  serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'id', 'last_login' , 'images']