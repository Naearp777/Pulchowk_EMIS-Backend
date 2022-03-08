from department.models import department
from notice.serializers import AssignmentNoticeSerializer, DepartmentNoticeSerializer, NoticeSerializer, GlobalNoticeSerializer
from .models import Assignmentnotice, Department_Notice, notice, Global_Notice
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
            publish_by=User.objects.get(id=t_id),
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
        shownotice = notice.objects.filter(publish_to=c_id).order_by('-created_at')
        showassigmentnotice=Assignmentnotice.objects.filter(publish_to=c_id).order_by('-created_at')
        noticeserializer = NoticeSerializer(shownotice, many=True)
        assigmentnoticeserializer = AssignmentNoticeSerializer(showassigmentnotice, many=True)
        return Response(
            {
                "notice": noticeserializer.data,
                "assignmentnotice": assigmentnoticeserializer.data,
            },status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_globalnotice(request):
    data = request.data
    print(data)
    try:
        Global_Notice.objects.create(
            title=data["title"],
            content=data["content"],
            files=request.FILES.get("files"),
            publish_by=User.objects.get(id=data["publish_by"]),
        )

        # if data["publish_to"] == "all":
        #     for i in User.objects.all():
        #         global_n.publish_to.add(i)

        # elif data["publish_to"] == "teacher":
        #     for i in User.objects.filter(staff=True):
        #         global_n.publish_to.add(i)

        # elif data["publish_to"] == "student":
        #     for i in User.objects.filter(student=True):
        #         global_n.publish_to.add(i)
                
        # elif data["publish_to"] == "department":
        #     for i in User.objects.filter(department=True):
        #         global_n.publish_to.add(i)
                

        # global_n.save()

        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_globalnotice(request, pk):
    try:
        shownotice = Global_Notice.objects.get(id=pk)
        serializer = GlobalNoticeSerializer(shownotice, many=False)
        return Response(serializer.data)

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_globalnotices(request): 
    shownotice = Global_Notice.objects.all()
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
        Global_Notice.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_globalnotice(request, pk):
    try:
        update_notice = Global_Notice.objects.get(id=pk)
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_deptnotice(request):
    data = request.data

    try:
        Department_Notice.objects.create(
            title=data["title"],
            content=data["content"],
            files=request.FILES.get("files"),
            publish_to=department.objects.get(name=data["publish_to"]),
            publish_by=User.objects.get(id=data["publish_by"]),
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_deptnotice(request, pk):
    shownotice = Department_Notice.objects.get(id=pk)
    serializer = DepartmentNoticeSerializer(shownotice, many=False)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_deptnotice_all_for_a_dept(request, alias):
    dept = department.objects.get(alias=alias)
    shownotice = Department_Notice.objects.filter(publish_to=dept.id)
    serializer = DepartmentNoticeSerializer(shownotice, many=True)
    return Response(serializer.data)

    