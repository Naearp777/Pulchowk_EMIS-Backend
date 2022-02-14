from ast import alias
from pyexpat import model
from django.shortcuts import render
from .models import department
from .serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['POST'])
def createdepartment(request):
    data=request.data
    try:
        newdepartment=department.objects.create(
            name=data['department_name'],
            description=data['description'],
            alias=data['alias']
        )
        serializer=DepartmentSerializer(newdepartment,many=False)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Department_display_all(request):
    all_departments = department.objects.all()
    serializer = DepartmentSerializer(all_departments, many=True)
    return Response(serializer.data)