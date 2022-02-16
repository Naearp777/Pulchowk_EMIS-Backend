from notice.serializers import NoticeSerializer, GlobalNoticeSerializer
from .models import notice, global_notice
from classes.models import classes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from customuser.models import User
from notification.models import Notification

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createnotice_teacher(request, c_id, t_id):
    data = request.data
    try:
        notice.objects.create(
            title=data["title"],
            content=data["content"],
            files=request.FILES.get("files"),
            publish_to=classes.objects.get(id=c_id),
            publish_by=str(User.objects.get(id=t_id).first_name)
            + " "
            + str(User.objects.get(id=t_id).last_name),
        )
        temp_list = len(classes.objects.get(id=c_id).student.all())
        for i in range(temp_list):
            Notification.objects.create(
                title=data["title"],
                content=data["content"],
                # publish to all students in the class in a list
                publish_to=(
                    User.objects.get(
                        id=classes.objects.get(id=c_id).student.all()[i].id
                    )
                ),
                publish_by=str(User.objects.get(id=t_id).first_name)
                + " "
                + str(User.objects.get(id=t_id).last_name),
            )
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_notice(request, c_id):
    try:
        shownotice = notice.objects.filter(publish_to=c_id)
        serializer = NoticeSerializer(shownotice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_globalnotice(request):
    data = request.data
    try:
        global_notice.objects.create(
            title=data["title"],
            content=data["content"],
            files=request.FILES.get("files"),
            publish_to=User.objects.all(),
            publish_by=data["publish_by"],
        )
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_globalnotice(request, pk):
    shownotice = global_notice.objects.filter(publish_to=pk)
    serializer = GlobalNoticeSerializer(shownotice, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_notice(request, pk):
    try:
        notice.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_notice(request, pk):
    try:
        update_notice = notice.objects.get(id=pk)
        data = request.data
        update_notice.title = data["title"]
        update_notice.content = data["content"]
        update_notice.files = request.FILES.get("files")
        update_notice.publish_to = classes.objects.get(id=data["publish_to"])
        update_notice.publish_by = data["publish_by"]
        update_notice.save()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_globalnotice(request, pk):
    try:
        global_notice.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_globalnotice(request, pk):
    try:
        update_notice = global_notice.objects.get(id=pk)
        data = request.data
        update_notice.title = data["title"]
        update_notice.content = data["content"]
        update_notice.files = request.FILES.get("files")
        update_notice.publish_to = User.objects.get(id=data["publish_to"])
        update_notice.publish_by = data["publish_by"]
        update_notice.save()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
