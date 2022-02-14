from rest_framework import  serializers

from .models import Give_Assignments,Submit_Assignments


class Give_AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Give_Assignments
        fields = '__all__'


class Submit_AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Submit_Assignments
        fields = '__all__'