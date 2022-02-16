from rest_framework import serializers

from classes.serializer import ClassSerializer
from customuser.serializers import UserSerializer_std

from .models import folder, materials


class FolderSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(read_only=True, many=False)
    teacher = UserSerializer_std(read_only=True, many=False)

    class Meta:
        model = folder
        fields = "__all__"


class MaterialsSerializer(serializers.ModelSerializer):
    folder = FolderSerializer(read_only=True, many=False)

    class Meta:
        model = materials
        fields = "__all__"
