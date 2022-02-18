from rest_framework import serializers

from .models import Assessment, student_info


class studentserializer_assessment(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = ['rollno','full_name']


class StudentSerializer_export(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = ["rollno", "student", "full_name"]


class AssessmentSerializer(serializers.ModelSerializer):

    student = studentserializer_assessment(read_only=True, many=False)

    class Meta:
        model = Assessment
        fields = "__all__"

