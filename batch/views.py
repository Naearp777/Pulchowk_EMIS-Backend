from django.shortcuts import render
from .models import Batch
from .serializers import BatchSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def show_batch(request):
    if request.method == 'GET':
        batch = BatchSerializer(Batch.objects.all(), many=True)
        return Response(batch.data)