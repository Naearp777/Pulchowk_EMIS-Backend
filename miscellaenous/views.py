from django.shortcuts import render
from customuser.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
import django_filters
from student.models import student_info

from student.serializers import StudentSerializer_search
from teacher.models import Teachers_info
from teacher.serializers import TeacherSerialize_search


# Create your views here

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def password_reset(request,u_id):
    data=request.data
    try:
        user=User.objects.get(id=u_id)
        user.password=make_password(data['password'])
        user.save()
        return Response({"message":"Password Changed successfully"},status=status.HTTP_200_OK)
    except:
        return Response({"message":"Password Not Changed"},status=status.HTTP_400_BAD_REQUEST)
    



class StudentFilter(django_filters.FilterSet):


    class Meta:
        model = student_info
        fields = ['department','batch','section']


# @permission_classes([IsAuthenticated])
class filter_student(ListAPIView):
    queryset = student_info.objects.all()
    serializer_class = StudentSerializer_search
    filter_class = StudentFilter

class TeachertFilter(django_filters.FilterSet):


    class Meta:
        model = Teachers_info
        fields = ['department']


# @permission_classes([IsAuthenticated])
class filter_teacher(ListAPIView):
    queryset = Teachers_info.objects.all()
    serializer_class = TeacherSerialize_search
    filter_class = TeachertFilter