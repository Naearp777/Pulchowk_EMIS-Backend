from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import section
from .serializers import SectionSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def section_display_all(request):
    all_section = section.objects.all()
    serializer = SectionSerializer(all_section, many=True)
    return Response(serializer.data)

@api_view([ 'POST'])
@permission_classes([IsAuthenticated])
def section_create(request):
    data = request.data
    try:
        section.objects.create(
            name=data['name'],
        )
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
