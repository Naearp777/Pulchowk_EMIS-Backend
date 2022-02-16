from classes.models import classes
from customuser.models import User
from .serializer import ClassSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_class(request):
    data = request.data
    print(data)
    try:
        newclass = classes.objects.create(
            name=data['class_name'],
        )
        showclass=classes.objects.get(name=data['class_name'])
      
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
       



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_class(request,pk):
    showclass=classes.objects.get(id=pk)
    serializer = ClassSerializer(showclass, many=False)
    return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_class(request):
    all_classes = classes.objects.all()
    serializer = ClassSerializer(all_classes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_class_by_teacher(request,pk):
    showclass=classes.objects.filter(teacher=pk)
    serializer = ClassSerializer(showclass, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_class_by_student(request,pk):
    showclass=classes.objects.filter(student=pk)
    serializer = ClassSerializer(showclass, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_class_by_department(request,pk):
    showclass=classes.objects.filter(department=pk)
    serializer = ClassSerializer(showclass, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_class(request,pk):
    data = request.data
    try:
        classes.objects.filter(id=pk).update(
            name=data['class_name'],
            teacher=data['t_id'],
            student=data['s_id'],
        )
        return Response({"message":"Class updated successfully"},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response( {"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_class(request,pk):
    try:
        classes.objects.filter(id=pk).delete()
        return Response({"message":"Class deleted successfully"},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response( {"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)
       


