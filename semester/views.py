from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response

from .serializers import SemesterSerializer
from .models import Semester
# Create your views here.

@api_view(['POST'])
def add_sem(request):
    try:
        sem = SemesterSerializer(Semester.objects.create() , many = False)
        return Response(sem.data , status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)