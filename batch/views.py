from logging import exception
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import batch
from .serializers import BatchSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Batch_display_all(request):
    all_batch = batch.objects.all()
    serializer = BatchSerializer(all_batch, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Batch_create(request):
    data=request.data
    try:
        batch.objects.create(
            name=data['name'],
        )
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response( {"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def Batch_update(request,id):
    data=request.data
    try:
        batch.objects.filter(id=id).update(
            name=data['name'],
        )
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response( {"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Batch_delete(request,id):
    try:
        batch.objects.filter(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response( {"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)