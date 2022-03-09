from rest_framework import serializers
from assignments.serializers import Give_AssignmentsSerializer

from classes.serializer import ClassSerializer
from customuser.serializers import UserSerializer_std
from department.serializers import DepartmentSerializer

from .models import Department_Notice, Global_Notice, notice,Assignmentnotice


class NoticeSerializer(serializers.ModelSerializer):
    publish_to = ClassSerializer(read_only=True, many=False)
    publish_by = UserSerializer_std(read_only=True, many=False)

    class Meta:
        model = notice
        fields = "__all__"
        
class AssignmentNoticeSerializer(serializers.ModelSerializer):
    assignment = Give_AssignmentsSerializer(read_only=True, many=False)
    publish_to = ClassSerializer(read_only=True, many=False)
    publish_by = UserSerializer_std(read_only=True, many=False)

    class Meta:
        model = Assignmentnotice
        fields = "__all__"
        
        


class GlobalNoticeSerializer(serializers.ModelSerializer):
    publish_by = UserSerializer_std(read_only=True, many=False)

    class Meta:
        model = Global_Notice
        fields = "__all__"


class DepartmentNoticeSerializer(serializers.ModelSerializer):
    publish_to = DepartmentSerializer(read_only=True, many=False)
    publish_by = UserSerializer_std(read_only=True, many=False)

    class Meta:
        model = Department_Notice
        fields = "__all__"
        
