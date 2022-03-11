from batch.models import batch
from classes.models import classes
from customuser.models import User
from department.models import Departmentadmin_info, department
from section.models import section
from student.models import student_info
from student.serializers import StudentSerializer, StudentSerializer_search
from .serializer import ClassSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_class(request):
    data = request.data
    print(data)
    try:
        newclass = classes.objects.create(
            name=data["class_name"],
            alias=data["alias"],
            department=department.objects.get(alias=data["department"]),
            batch=batch.objects.get(name=data["batch"]),
            section=section.objects.get(name=data["section"]),
        )
        showclass = classes.objects.get(id=newclass.id)

        print(data["t_id"])
        for t in data["t_id"]:
            print(t)
            t = User.objects.get(id=t)
            showclass.teacher.add(t)
            showclass.save()

        for s in student_info.objects.filter(
            department=department.objects.get(alias=data["department"]),
            batch=batch.objects.get(name=data["batch"]),
            section=section.objects.get(name=data["section"]),
        ):
            print("s", s.student.id)
            s = User.objects.get(id=s.student.id)
            showclass.student.add(s)
            showclass.save()

        serializer = ClassSerializer(newclass, many=False)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_class(request, pk):
    showclass = classes.objects.get(id=pk)
    serializer = ClassSerializer(showclass, many=False)
    return Response(serializer.data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_class(request):
    all_classes = classes.objects.all()
    serializer = ClassSerializer(all_classes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_students_in_a_class(request, pk):
    showclass = classes.objects.get(id=pk)
    serializer = ClassSerializer(showclass, many=False)
    students = []

    for s in serializer.data["student"]:
        s_info = student_info.objects.get(student=s.get("id"))
        students.append(StudentSerializer(student_info.objects.get(student=s.get("id")), many=False).data)
        
    return Response(students)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_class_by_teacher(request, pk):
    showclass = classes.objects.filter(teacher=pk)
    serializer = ClassSerializer(showclass, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_class_by_student(request, pk):
    showclass = classes.objects.filter(student=pk)
    serializer = ClassSerializer(showclass, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_class_by_department(request, pk):
    dept = Departmentadmin_info.objects.get(dept_admin=pk)
    showclass = classes.objects.filter(department=dept.department)
    serializer = ClassSerializer(showclass, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_class(request, pk):
    data = request.data
    try:
        classes.objects.filter(id=pk).update(
            name=data["class_name"],
            teacher=data["t_id"],
            student=data["s_id"],
        )
        return Response(
            {"message": "Class updated successfully"}, status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_class(request, pk):
    try:
        classes.objects.filter(id=pk).delete()
        return Response(
            {"message": "Class deleted successfully"}, status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
