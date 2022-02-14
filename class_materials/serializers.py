from rest_framework import  serializers

from .models import folder,materials


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = folder
        fields = '__all__'


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = materials
        fields = '__all__'