from rest_framework import  serializers

from customuser.serializers import UserSerializer_std

from .models import  Give_Assignments,Submit_Assignments
from classes.serializer import ClassSerializer


class Give_AssignmentsSerializer(serializers.ModelSerializer):
    classes=ClassSerializer(read_only=True, many=False)
    teacher=UserSerializer_std(read_only=True, many=False)

    class Meta:
        model =Give_Assignments
        fields = '__all__'


class Submit_AssignmentsSerializer(serializers.ModelSerializer):
    student=UserSerializer_std(read_only=True, many=False)
    assignment=Give_AssignmentsSerializer(read_only=True, many=False)
    class Meta:
        model =Submit_Assignments
        fields = '__all__'

class Calendar_Give_AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Give_Assignments
        exclude=['created_at','updated_at','teacher_files','classes','teacher']
