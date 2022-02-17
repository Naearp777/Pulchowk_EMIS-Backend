from rest_framework import serializers

from classes.serializer import ClassSerializer

from .models import global_notice, notice,Assignmentnotice


class NoticeSerializer(serializers.ModelSerializer):
    publish_to = ClassSerializer(read_only=True, many=False)

    class Meta:
        model = notice
        fields = "__all__"
        
class AssignmentNoticeSerializer(serializers.ModelSerializer):
    publish_to = ClassSerializer(read_only=True, many=False)

    class Meta:
        model = Assignmentnotice
        fields = "__all__"
        
        


class GlobalNoticeSerializer(serializers.ModelSerializer):
    publish_to = ClassSerializer(read_only=True, many=False)

    class Meta:
        model = global_notice
        fields = "__all__"
        
