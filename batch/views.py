from logging import exception
from django.shortcuts import render
from .models import Batch
from .serializers import BatchSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from batch import serializers
# Create your views here.
@api_view(['GET']) 
def show_batch(request):
    batch = BatchSerializer(Batch.objects.all(), many=True)
    return Response(batch.data , status=status.HTTP_200_OK)

class AddBatch(generics.CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    # permission_classes = (IsAuthenticated,)
    
@api_view(['POST'])
def add_batch(request):
    try :
        data = request.data
        batch  = BatchSerializer(Batch.objects.create(
            batch_YR = data['batch_YR'],
            ) , many = False)
        return Response(batch.data , status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)    

@api_view(['DELETE'])
def destroy_batch(request, pk):
    try :
        if request.method == 'DELETE':
            batch = Batch.objects.get(pk=pk)
            batch.delete()
            message  = {"message" : "Batch Deleted Successfully"}
            return Response( message , status=status.HTTP_204_NO_CONTENT)
    except:
        message  = {"message" : "Could not delete batch"}
        return Response(message ,  status=status.HTTP_400_BAD_REQUEST)

# class DestroyBatch(generics.DestroyAPIView):
#     queryset = Batch.objects.all()
#     serializer = BatchSerializer
    
@api_view(['PUT'])
def update_batch(request, pk):
    try:
        batch = Batch.objects.get(pk=pk)
    except Batch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BatchSerializer(batch, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

