from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from classes.models import classes
from student.models import student_info
from .serializers import AttendanceSerializer
from customuser.models import ExcelFileUpload
from django.conf import settings
import pandas as pd


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def importattendance_csv(request, c_id):
    try:
        data = request.data
        excel_upload = ExcelFileUpload.objects.create()
        excel_upload.excel_file = request.FILES.get("file")
        excel_upload.save()
        df = pd.read_csv(f"{settings.BASE_DIR}/media/{excel_upload.excel_file}")
        for data in df.values.tolist():
            Attendance.objects.create(
                classes=classes.objects.get(id=c_id),
                student=student_info.objects.get(rollno=data[1]),
                date=data[0],
                status=data[2],
            )
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_attendance_list(request, c_id):
    try:
        data = request.data
        users = Attendance.objects.filter(classes=classes.objects.get(id=c_id))
        serializer = AttendanceSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def delete_attendance_list(request, c_id):
    try:
        data = request.data
        Attendance.objects.filter(classes=classes.objects.get(id=c_id)).delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_attendance_list_by_date(request, c_id, date):
    try:
        data = request.data
        users = Attendance.objects.filter(
            classes=classes.objects.get(id=c_id), date=date
        )
        serializer = AttendanceSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_total_working_days(request, c_id):
    try:
        data = request.data
        users = (
            Attendance.objects.filter(classes=classes.objects.get(id=c_id))
            .values("date")
            .distinct()
            .count()
        )
        return Response({"total_working_days": users}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_student_present_days(request, c_id, s_id):
    try:
        data = request.data
        users = (
            Attendance.objects.filter(
                classes=classes.objects.get(id=c_id),
                student=student_info.objects.get(id=s_id),
            )
            .values("date")
            .distinct()
            .count()
        )
        return Response({"student_present_days": users}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
