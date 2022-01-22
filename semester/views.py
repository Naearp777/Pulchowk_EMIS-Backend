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
        data = request.data
        print(data)
        sem = SemesterSerializer(
            Semester.objects.create(
                sem_name  = data['sem_name'],
                sem_start_date = data['sem_start_date'],
                sem_end_date = data['sem_end_date'],
                year = data['year'],
                part  = data['part'],
                ) , many = False)
        return Response(sem.data , status=status.HTTP_201_CREATED)
    except Exception as e:
        message  = {"message" : str(e)}
        return Response( message ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET' , 'DELETE' , 'PUT'])
def sem_detail(request , pk):
    try:
        sem = Semester.objects.get(pk=pk)
    except Semester.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        sem = SemesterSerializer(sem , many=False)
        return Response(sem.data , status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = request.data
        sem = SemesterSerializer(sem , data=data)
        if sem.is_valid():
            sem.save()
            return Response(sem.data , status=status.HTTP_200_OK)
        return Response(sem.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sem.delete()
        message  = {"message" : "Semester Deleted Successfully"}
        return Response(message , status=status.HTTP_204_NO_CONTENT)
    
class AddSem(generics.CreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    # permission_classes = (IsAuthenticated,)