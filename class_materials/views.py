from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from class_materials.models import materials,folder
from classes.models import classes
from customuser.models import User
from rest_framework.decorators import api_view
from .serializers import MaterialsSerializer,FolderSerializer
# Create your views here.
@api_view(['POST'])
def upload_materials(request,f_id):
    data=request.data
    files  = request.FILES.getlist('files')
    try:
        for file in files: 
            materials.objects.create(
                folder=folder.objects.get(id=f_id),
                file=file,
                created_at=data['created_at'],
                updated_at=data['updated_at'],
                )
        return Response({"message":"Materials uploaded successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response({"message":"Materials not uploaded"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_folder(request,c_id,t_id):
    data=request.data
    try:
        folder.objects.create(
            classes=classes.objects.get(id=c_id),
            folder_name=data['folder_name'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
            teacher=User.objects.get(id=t_id),
        )
        return Response({"message":"Folder created successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response({"message":"Folder not created"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_folder(request,pk):
    data=request.data
    try:
        folder.objects.filter(id=pk).update(
            folder_name=data['folder_name'],
            updated_at=data['updated_at'],
        )
        return Response({"message":"Folder updated successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response({"message":"Folder not updated"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_folder(request,pk):
    try:
        folder.objects.filter(id=pk).delete()
        return Response({"message":"Folder deleted successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response({"message":"Folder not deleted"},status=status.HTTP_400_BAD_REQUEST)

