from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from teacher.models import Teachers_info
from .serializers import TeacherSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_teacher(request):
    all_teachers = Teachers_info.objects.all()
    serializer = TeacherSerializer(all_teachers, many=True)
    return Response(serializer.data)