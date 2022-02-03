from pyexpat import model
from django.shortcuts import render
from .models import department
from .serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def createdepartment(request):
    data=request.data
    try:
        newdepartment=department.objects.create(
            department_name=data['department_name'],
            description=data['description']
        )
        serializer=DepartmentSerializer(newdepartment,many=False)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
