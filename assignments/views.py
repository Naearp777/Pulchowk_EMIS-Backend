from pickle import APPEND
from turtle import title
from django.shortcuts import render
from assignments.models import Give_Assignments,Submit_Assignments
from customuser.models import User
from classes.models import classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def create_assignment(request,c_id,t_id):
    data=request.data
    try:
        Give_Assignments.objects.create(
        classes=classes.objects.get(id=c_id),
        teacher=User.objects.get(id=t_id),
        title=data['title'],
        description=data['description'],
        due_date=data['due_date'],
        completed=data['completed'],
        created_at=data['created_at'],
        updated_at=data['updated_at'],
        teacher_files=request.FILES.get('teacher_files'),
        )
        return Response ({"message":"Assignment created successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response ({"message":"Assignment not created"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_assignment(request,a_id,s_id):
    data=request.data
    try:
        Submit_Assignments.objects.create(
        student=User.objects.get(id=s_id),
        assignment=Give_Assignments.objects.get(id=a_id),
        student_files=request.FILES.get('student_files'),
        )
        return Response ({"message":"Assignment submitted successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response ({"message":"Assignment not submitted"},status=status.HTTP_400_BAD_REQUEST)
