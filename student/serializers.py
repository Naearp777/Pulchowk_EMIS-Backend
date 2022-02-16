from rest_framework import serializers
from batch.serializers import BatchSerializer

from customuser.serializers import UserSerializer_std
from department.serializers import DepartmentSerializer
from section.serializers import SectionSerializer

from .models import student_info


class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer_std(read_only=True, many=False)
    department = DepartmentSerializer(read_only=True, many=False)
    batch = BatchSerializer(read_only=True, many=False)
    section = SectionSerializer(read_only=True, many=False)

    class Meta:
        model = student_info
        fields = "__all__"


class StudentSerializer_search(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = "__all__"
