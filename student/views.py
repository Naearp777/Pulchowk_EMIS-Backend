from urllib import response
from django.shortcuts import render
from customuser.models import User
from student.models import student_info
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def show_all_students(request):
    all_students = student_info.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)


 