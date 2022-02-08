from urllib import response
from django.shortcuts import render
from .models import notice
from classes.models import classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from customuser.models import User
# Create your views here.


@api_view(['POST'])
def createnotice(request):
  data=request.data
  try:
    notice.objects.create(
      title=data['title'],
      content=data['content'],
      files=request.FILES.get('files'),
      publish_to=classes.objects.get(class_name=data['class_name']),
        publish_by=User.objects.get(email=data['email'])
      
    )
    return Response(status=status.HTTP_201_CREATED)
  except:
    return Response(status=status.HTTP_400_BAD_REQUEST)
        