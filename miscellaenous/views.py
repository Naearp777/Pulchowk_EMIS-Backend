from django.shortcuts import render
from customuser.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here

@api_view(['POST'])
def password_reset(request,u_id):
    data=request.data
    try:
        user=User.objects.get(id=u_id)
        user.password=make_password(data['password'])
        user.save()
        return Response({"message":"Password Changed successfully"},status=status.HTTP_200_OK)
    except:
        return Response({"message":"Password Not Changed"},status=status.HTTP_400_BAD_REQUEST)
    



