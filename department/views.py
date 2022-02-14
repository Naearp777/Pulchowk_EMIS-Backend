from django.shortcuts import render
from .models import department
from .serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createdepartment(request):
    data=request.data
    try:
        newdepartment=department.objects.create(
            name=data['department_name'],
            description=data['description'],
            alias=data['alias']
        )
        serializer=DepartmentSerializer(newdepartment,many=False)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response( {"message" : str(e) } , status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Department_display_all(request):
    try :
        all_departments = department.objects.all()
        serializer = DepartmentSerializer(all_departments, many=True)
        return Response(serializer.data  ,status= status.HTTP_200_OK)
    except Exception as e:
        return Response( {"message" : str(e) } , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Department_display_by_id(request,pk):
    try:
        showdepartment=department.objects.get(id=pk)
        serializer=DepartmentSerializer(showdepartment,many=False)
        return Response(serializer.data , status  = status.HTTP_200_OK)
    except Exception as e:
        return Response ({"message" : str(e) } , status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Department_display_by_alias(request,alias):
    try:
        showdepartment=department.objects.get(alias=alias)
        serializer=DepartmentSerializer(showdepartment,many=False)
        return Response(serializer.data , status  = status.HTTP_200_OK)
    except Exception as e:
        return Response ({"message" : str(e) } , status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def Department_update(request,pk):
    data=request.data
    try:
        updatedepartment=department.objects.get(id=pk)
        updatedepartment.name=data['department_name']
        updatedepartment.description=data['description']
        updatedepartment.alias=data['alias']
        updatedepartment.save()
        serializer=DepartmentSerializer(updatedepartment,many=False)
        return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response( {"message" : str(e)} , status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Department_delete(request,pk):
    try:
        deletedepartment=department.objects.get(id=pk)
        deletedepartment.delete()
        return Response({"message": "Department has been deleted sucessfully."}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response( {"message" : str(e)} , status=status.HTTP_400_BAD_REQUEST)