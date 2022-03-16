from customuser.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
import django_filters
from department.models import Departmentadmin_info, department
from student.models import student_info

from student.serializers import StudentSerializer, StudentSerializer_search
import teacher
from teacher.models import Teachers_info
from teacher.serializers import TeacherSerialize_search
from classes.models import classes
from .models import EvaluationForm
from assignments.models import Give_Assignments, Submit_Assignments
from assignments.serializers import (
    Submit_AssignmentsSerializer,
    Calendar_Give_AssignmentsSerializer,
)
from datetime import datetime
from attendance.models import Attendance

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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_department_dashboard(request, alias):
    dept = department.objects.get(alias=alias)
    students = student_info.objects.filter(department=dept.id).count()
    teachers = Teachers_info.objects.filter(department=dept.id).count()
    classNo = classes.objects.filter(department=dept.id).count()
    studentMale = student_info.objects.filter(student__gender="Male").count()
    teacherMale = Teachers_info.objects.filter(teacher__gender="Male").count()

    data = {
        "students": {
            "male": studentMale,
            "female": students - studentMale,
            "total": students,
        },
        "teachers": {
            "male": teacherMale,
            "female": teachers - teacherMale,
            "total": teachers,
        },
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
def evaluate_students_by_evaluation_form_for_specific_student(request, c_id, s_id):
    try:
        total_marks_obtained = 0
        total_marks = 0
        showassignment = Give_Assignments.objects.filter(classes=c_id)
        serializer = Calendar_Give_AssignmentsSerializer(showassignment, many=True)
        for assignment in serializer.data:
            if str(assignment["due_date"]) <= str(datetime.now()):
                total_marks += assignment["total_points"]
        showassignment = Submit_Assignments.objects.filter(
            assignment__classes=c_id, student=s_id
        )
        serializer = Submit_AssignmentsSerializer(showassignment, many=True)

        assignmentsData = []

        for assignment in serializer.data:
            if str(assignment["assignment"]["due_date"]) <= str(datetime.now()):
                total_marks_obtained += assignment["obtain_points"]
                assignmentsData.append(assignment)

        Total_working_days = (
            Attendance.objects.filter(classes=classes.objects.get(id=c_id))
            .values("date")
            .distinct()
            .count()
        )
        print("addddddd")
        std = User.objects.get(id=s_id)
        Present_days = (
            Attendance.objects.filter(
                classes=classes.objects.get(id=c_id),
                student=student_info.objects.get(student=std.id),
                status=True,
            )
            .values("date")
            .distinct()
            .count()
        )
        print(total_marks)
        print(total_marks_obtained)
        print(Total_working_days)
        print(Present_days)
        evaluation = EvaluationForm.objects.get(classes=c_id)
        if Total_working_days == 0 | total_marks == 0:
            performance_points = 0
        else:
            performance_points = (
                total_marks_obtained * evaluation.assignment_percentage
            ) / (100 * total_marks) + (
                Present_days * evaluation.attendance_percentage
            ) / (
                100 * Total_working_days
            )
            p = format(performance_points * 100, ".2f")
            data = {
                "total_marks": total_marks,
                "total_marks_obtained": total_marks_obtained,
                "total_working_days": Total_working_days,
                "present_days": Present_days,
                "attendance_percentage": evaluation.attendance_percentage,
                "assignment_percentage": evaluation.assignment_percentage,
                "performance_points": p,
                "assignments": assignmentsData,
            }

        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"message": str(e)},
            status=status.HTTP_400_BAD_REQUEST,
        )
