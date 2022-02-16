from rest_framework import serializers

from department.serializers import DepartmentSerializer

from .models import Teachers_info
from customuser.serializers import UserSerializer_std


class TeacherSerializer(serializers.ModelSerializer):
    teacher = UserSerializer_std(read_only=True, many=False)
    department = DepartmentSerializer(read_only=True, many=False)

    class Meta:
        model = Teachers_info
        fields = "__all__"


class TeacherSerialize_search(serializers.ModelSerializer):
    class Meta:
        model = Teachers_info
        fields = "__all__"
