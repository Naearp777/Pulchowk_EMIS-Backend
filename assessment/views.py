from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import pandas as pd
from department.models import department
from student.models import student_info
from .models import Assessment
from classes.models import classes
from customuser.models import ExcelFileUpload
from django.conf import settings
from .serializers import AssessmentSerializer, StudentSerializer_export
from batch.models import batch
from section.models import section

# Create your views here.


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def importassessment_csv(request, c_id):
    try:
        data = request.data
        excel_upload = ExcelFileUpload.objects.create()
        excel_upload.excel_file = request.FILES.get("file")
        excel_upload.save()
        df = pd.read_csv(f"{settings.BASE_DIR}/media/{excel_upload.excel_file}")
        for data in df.values.tolist():
            Assessment.objects.create(
                classes=classes.objects.get(id=c_id),
                student=student_info.objects.get(rollno=data[0]),
                marks=data[1],
            )
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def Export_Student_Class_list(request, d_id):
    try:
        data = request.data
        users = student_info.objects.filter(
            department=department.objects.get(id=d_id),
            batch=batch.objects.get(name=data["batch"]),
            section=section.objects.get(name=data["section"]),
        )
        serializer = StudentSerializer_export(users, many=True)
        df = pd.DataFrame(serializer.data)
        df.to_csv("media/excel/export.csv", index=False)
        # print(df)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_assessment_list(request, c_id):
    try:
        users = Assessment.objects.filter(classes=classes.objects.get(id=c_id))
        serializer = AssessmentSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def delete_assessment(request, c_id):
    try:
        users = Assessment.objects.filter(classes=classes.objects.get(id=c_id))
        users.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def delete_assessment_by_id(request, a_id):
    try:
        users = Assessment.objects.get(id=a_id)
        users.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
