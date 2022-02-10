from rest_framework import  serializers

from .models import Teachers_info


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers_info
        fields = '__all__'