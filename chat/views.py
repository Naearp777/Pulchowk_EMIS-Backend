
from .models import Messages
from customuser.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import MessagesSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
# Create your views here.
#send message from sender to receiver
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def sendMessage(request,sender,receiver):
    data = request.data
    message = Messages.objects.create(
        sender=User.objects.get(id=sender),
        receiver=User.objects.get(id=receiver),
        msg=data["msg"],
        timestamp=data["timestamp"]
    )
    serializer = MessagesSerializer(message, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getMessage(request,sender,receiver):
    sender = User.objects.get(id=sender)
    receiver = User.objects.get(id=receiver)
    message=Messages.objects.filter( 
        Q(sender = sender , receiver=receiver) | 
        Q(sender = receiver,receiver=sender))

    serializer = MessagesSerializer(message, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getMessageBySender(request,sender):
    sender = User.objects.get(id=sender)
    message = Messages.objects.filter(
        sender=sender,
    )
    serializer = MessagesSerializer(message, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getMessageByReceiver(request,receiver):
    receiver = User.objects.get(id=receiver)
    message = Messages.objects.filter(
        receiver=receiver,
    )
    serializer = MessagesSerializer(message, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)







   