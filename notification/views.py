
from .serializers import NotificationSerializer
from .models import Notification
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from customuser.models import User
from assignments.models import Assignment

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_notification_to_user(request,pk):
    try:
        all_notification = Notification.objects.filter(publish_to=pk)
        serializer = NotificationSerializer(all_notification, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)

