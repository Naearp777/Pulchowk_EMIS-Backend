from customuser.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
import django_filters
from department.models import Departmentadmin_info
from student.models import student_info

from student.serializers import StudentSerializer_search
import teacher
from teacher.models import Teachers_info
from teacher.serializers import TeacherSerialize_search
from classes.models import classes
from .models import EvaluationForm


# Create your views here


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def password_reset(request, u_id):
    data = request.data
    try:
        user = User.objects.get(id=u_id)
        user.password = make_password(data["password"])
        user.save()
        return Response(
            {"message": "Password Changed successfully"}, status=status.HTTP_200_OK
        )
    except:
        return Response(
            {"message": "Password Not Changed"}, status=status.HTTP_400_BAD_REQUEST
        )


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = student_info
        fields = ["department", "batch", "section"]


@permission_classes([IsAuthenticated])
class filter_student(ListAPIView):
    queryset = student_info.objects.all()
    serializer_class = StudentSerializer_search
    filter_class = StudentFilter


class TeachertFilter(django_filters.FilterSet):
    class Meta:
        model = Teachers_info
        fields = ["department"]


@permission_classes([IsAuthenticated])
class filter_teacher(ListAPIView):
    queryset = Teachers_info.objects.all()
    serializer_class = TeacherSerialize_search
    filter_class = TeachertFilter


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_admin_dashboard(request):
    students = student_info.objects.all().count()
    teachers = Teachers_info.objects.all().count()
    dept_admins = Departmentadmin_info.objects.all().count()
    data = {
        "students": students,
        "teachers": teachers,
        "department_admins": dept_admins,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_student_dashboard(request, pk):
    classNo = classes.objects.filter(student=pk).count()
    data = {
        "classes": classNo,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_teacher_dashboard(request, pk):
    classNo = classes.objects.filter(teacher=pk).count()
    data = {
        "classes": classNo,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_evaluation_form(request, pk):
    try:
        data = request.data
        EvaluationForm.objects.create(
            classes=classes.objects.get(id=pk),
            attendance_percentage=data["attendance_percentage"],
            assignment_percentage=data["assignment_percentage"],
        )
        return Response(
            {"message": "Evaluation Form Created"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {"message": "Evaluation Form Not Created"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def evaluate_students_by_evaluation_form_for_specific_student(request, pk):
    pass
