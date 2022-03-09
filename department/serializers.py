from rest_framework import serializers

from customuser.serializers import UserSerializer_std

from .models import Departmentadmin_info, department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = "__all__"


class DepartmentAdminSerializer(serializers.ModelSerializer):
    dept_admin = UserSerializer_std(many=False, read_only=True)
    department = DepartmentSerializer(many=False, read_only=True)
    class Meta:
        model = Departmentadmin_info
        fields = "__all__"