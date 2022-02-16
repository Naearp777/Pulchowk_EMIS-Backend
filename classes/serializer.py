from rest_framework import serializers

from department.serializers import DepartmentSerializer

from .models import classes
from customuser.serializers import UserSerializer_std


class ClassSerializer(serializers.ModelSerializer):
    teacher = UserSerializer_std(read_only=True, many=True)
    student = UserSerializer_std(read_only=True, many=True)
    department = DepartmentSerializer(read_only=True, many=False)

    class Meta:
        model = classes
        fields = "__all__"
