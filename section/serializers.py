from re import S
from rest_framework import  serializers

from .models import section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = '__all__'