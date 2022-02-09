from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import batch
from .serializers import BatchSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Batch_display_all(request):
    all_batch = batch.objects.all()
    serializer = BatchSerializer(all_batch, many=True)
    return Response(serializer.data)