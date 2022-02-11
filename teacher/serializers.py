from rest_framework import  serializers

from department.serializers import DepartmentSerializer

from .models import Teachers_info


class TeacherSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer(read_only=True, many=False)
    class Meta:
        model = Teachers_info
        fields = '__all__'