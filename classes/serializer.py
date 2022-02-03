from rest_framework import  serializers

from .models import classes


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = classes
        fields = '__all__'