from batch.models import batch
from classes.models import classes
from customuser.models import User
from department.models import department
from section.models import section
from student.models import student_info
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
        temp_list=len(classes.objects.get(student_info.objects.filter(department=department.objects.get(id=data['department_id']),batch=batch.objects.get(id=data['batch_id']),section=section.objects.get(id=data['section_id'])).all()))
        for i in range(temp_list):
            newclass = classes.objects.create(
                name=data['class_name'],
                student=User.objects.get(id=student_info.objects.filter(department=department.objects.get(id=data['department_id']),batch=batch.objects.get(id=data['batch_id']),section=section.objects.get(id=data['section_id'])).all()[i].id),
            )
            showclass=classes.objects.get(name=data['class_name'])
      
        print(data['t_id'])
        for t in data['t_id'].split(","):
            t = User.objects.get(id=t)
            showclass.teacher.add(t)
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
       


