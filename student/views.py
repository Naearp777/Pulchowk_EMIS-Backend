from student.models import student_info
from .serializers import StudentSerializer, StudentallSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_students(request):
    all_students = student_info.objects.all()
    serializer = StudentSerializer(all_students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_student_profile(request, s_id):
    try:
        student = student_info.objects.get(student_id=s_id)
        print("student")
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(
            {"message": "Student not found"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_student(request):
    all_students = student_info.objects.all()
    serializer = StudentallSerializer(all_students, many=True)
    return Response(serializer.data)


