from django.shortcuts import render
from classes.models import classes
from customuser.models import User
from .serializer import ClassSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def create_class(request):
    data = request.data
    print(data)
    try:
        newclass = classes.objects.create(
            class_name=data['class_name'],
        )
        showclass=classes.objects.get(class_name=data['class_name'])
      
        print(data['t_id'])
        for t in data['t_id'].split(","):
            t = User.objects.get(id=t)
            showclass.teacher.add(t)
            showclass.save()

        for s in data['s_id'].split(","):
            s = User.objects.get(id=s)
            showclass.student.add(s)
            showclass.save()

        
        
        serializer = ClassSerializer(newclass, many=False)
        print(serializer.data)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def show_class(request,pk):
    showclass=classes.objects.get(id=pk)
    serializer = ClassSerializer(showclass, many=False)
    return Response(serializer.data)