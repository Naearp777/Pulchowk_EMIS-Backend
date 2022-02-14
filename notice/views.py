from urllib import response
from django.shortcuts import render
from assignments import serializers

from notice.serializers import NoticeSerializer
from .models import notice
from classes.models import classes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from customuser.models import User
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createnotice_teacher(request,c_id):
  data=request.data
  try:
    notice.objects.create(
      title=data['title'],
      content=data['content'],
      files=request.FILES.get('files'),
      publish_to=classes.objects.get(id=c_id),
      publish_by=data['publish_by']
      
    )

    return Response(status=status.HTTP_201_CREATED)
  except Exception as e:
    return Response( {"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_notice(request,c_id):
  try:
    shownotice=notice.objects.filter(publish_to=c_id)
    serializer = NoticeSerializer(shownotice, many=True)
    return Response(serializer.data , status  = status.HTTP_200_OK)
  except Exception as e:
    return Response( {"message" : str(e)}, status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_globalnotice(request):
  data=request.data
  try:
    notice.objects.create(
      title=data['title'],
      content=data['content'],
      files=request.FILES.get('files'),
      publish_to=User.objects.all(),
      publish_by=data['publish_by']

    )
    return Response(status=status.HTTP_201_CREATED)
  except:
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_globalnotice(request,pk):
  shownotice=notice.objects.filter(publish_to=pk)
  serializer = NoticeSerializer(shownotice, many=True)
  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_notice(request,pk):
  try:
    notice.objects.get(id=pk).delete()
    return Response(status=status.HTTP_200_OK)
  except:
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_notice(request,pk):
  try:
    update_notice=notice.objects.get(id=pk)
    data=request.data
    update_notice.title=data['title']
    update_notice.content=data['content']
    update_notice.files=request.FILES.get('files')
    update_notice.publish_to=classes.objects.get(id=data['publish_to'])
    update_notice.publish_by=data['publish_by']
    update_notice.save()
    return Response(status=status.HTTP_200_OK)
  except:
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_globalnotice(request,pk):
  try:
    notice.objects.get(id=pk).delete()
    return Response(status=status.HTTP_200_OK)
  except:
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_globalnotice(request,pk):
  try:
    update_notice=notice.objects.get(id=pk)
    data=request.data
    update_notice.title=data['title']
    update_notice.content=data['content']
    update_notice.files=request.FILES.get('files')
    update_notice.publish_to=User.objects.get(id=data['publish_to'])
    update_notice.publish_by=data['publish_by']
    update_notice.save()
    return Response(status=status.HTTP_200_OK)
  except:
    return Response(status=status.HTTP_400_BAD_REQUEST)

