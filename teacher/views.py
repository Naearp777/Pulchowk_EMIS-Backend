from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from department.models import department
from teacher.models import Teachers_info
from .serializers import TeacherSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from classes.models import classes


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_teacher(request):
    all_teachers = Teachers_info.objects.all()
    serializer = TeacherSerializer(all_teachers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_teacher_by_department(request, alias):
    dept = department.objects.get(alias=alias)
    all_teachers = Teachers_info.objects.filter(department=dept)
    serializer = TeacherSerializer(all_teachers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_teacher_profile(request, t_id):
    teacher = Teachers_info.objects.get(teacher=t_id)
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_students_for_a_teacher(request, t_id):
    students = classes.objects.filter(teacher=t_id).values("student").distinct().count()
    print(students)

    data = {
        "students": students
    }

    return Response(data, status=status.HTTP_200_OK)
