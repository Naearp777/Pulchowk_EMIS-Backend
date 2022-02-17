from rest_framework import serializers
from assignments.serializers import Give_AssignmentsSerializer

from classes.serializer import ClassSerializer
from customuser.serializers import UserSerializer_std

from .models import global_notice, notice,Assignmentnotice


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
    publish_to = ClassSerializer(read_only=True, many=False)
    publish_by = UserSerializer_std(read_only=True, many=False)

    class Meta:
        model = global_notice
        fields = "__all__"
        
