from rest_framework import serializers


from customuser.serializers import UserSerializer_std

from classes.serializer import ClassSerializer
from student.serializers import StudentSerializer_search
from .models import Assessment, student_info




class StudentSerializer_export(serializers.ModelSerializer):
    

    class Meta:
        model = student_info
        fields = ['rollno']
        


class AssessmentSerializer(serializers.ModelSerializer):
    
    
    student=StudentSerializer_search(read_only=True, many=False)

    class Meta:
        model = Assessment
        fields = "__all__"