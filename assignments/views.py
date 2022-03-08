from notification.models import Notification
from .models import Give_Assignments, Submit_Assignments
from customuser.models import User
from classes.models import classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import (
    Give_AssignmentsSerializer,
    Submit_AssignmentsSerializer,
    Calendar_Give_AssignmentsSerializer,
)
from rest_framework.decorators import api_view
from notice.models import Assignmentnotice
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_assignment(request, c_id, t_id):
    data = request.data
    try:
        assignment = Give_Assignments.objects.create(
            classes=classes.objects.get(id=c_id),
            teacher=User.objects.get(id=t_id),
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            total_points=data["total_points"],
            teacher_files=request.FILES.get("teacher_files"),
        )
        Assignmentnotice.objects.create(
            assignment=Give_Assignments.objects.get(id = assignment.id),
            title=data["title"],
            content=data["description"],
            publish_to=classes.objects.get(id=c_id),
            publish_by=User.objects.get(id=t_id),
        )
        temp_list = len(classes.objects.get(id=c_id).student.all())
        for i in range(temp_list):
            Notification.objects.create(
                title=data["title"],
                content=data["description"],
                # publish to all students in the class in a list
                publish_to=(
                    User.objects.get(
                        id=classes.objects.get(id=c_id).student.all()[i].id
                    )
                ),
                publish_by=User.objects.get(id=t_id)
                
            )
        return Response(
            {"message": "Assignment created successfully"},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_assignment(request, a_id, s_id):
    data = request.data
    try:
        Submit_Assignments.objects.create(
            student=User.objects.get(id=s_id),
            assignment=Give_Assignments.objects.get(id=a_id),
            # obtain_points=data["obtain_points"],
            student_files=request.FILES.get("student_files"),
        )
        return Response(
            {"message": "Assignment submitted successfully"},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_assignment(request, pk):
    showassignment = Give_Assignments.objects.get(id=pk)
    serializer = Give_AssignmentsSerializer(showassignment, many=False)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_assignment_given_by_teacher_in_specific_class(request, t_id, c_id):
    showassignment = Give_Assignments.objects.filter(teacher=t_id, classes=c_id)
    serializer = Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_assignment_in_specific_class(request, c_id):
    showassignment = Give_Assignments.objects.filter(classes=c_id)
    serializer = Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_assignment_details_of_a_specific_assignment_for_a_student(request, a_id, s_id):
    assignmentData = Give_Assignments.objects.get(id=a_id)
    assignment = Give_AssignmentsSerializer(assignmentData, many=False)
    try:
        submissionData = Submit_Assignments.objects.get(
            assignment=a_id, student=s_id
        )
        submission = Submit_AssignmentsSerializer(submissionData, many=False)
        data = {
            "assignment": assignment.data,
            "submission": submission.data,
        }
        return Response(data, status=status.HTTP_200_OK)
    except:
        data = {
            "assignment": assignment.data,
            "submission": '',
        }
        return Response(data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_submitted_assignments_for_an_assignment(request, a_id):
    showassignment = Submit_Assignments.objects.filter(assignment=a_id)
    serializer = Submit_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_submitted_assignments_for_a_student(request, s_id):
    showassignment = Submit_Assignments.objects.filter(student=s_id)
    serializer = Submit_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_submitted_assignments_for_a_student_in_a_class(request, s_id, c_id):
    showassignment = Submit_Assignments.objects.filter(
        student=s_id, assignment__classes=c_id
    )
    serializer = Submit_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_assignment(request, pk):
    data = request.data
    try:
        updateassignment = Give_Assignments.objects.get(id=pk)
        if data["title"] :
            updateassignment.title = data["title"]
        if data["description"]:
            updateassignment.description = data["description"]
        if data["due_date"]:
            updateassignment.due_date = data["due_date"]
        if request.FILES.get("teacher_files"):
            updateassignment.teacher_files = request.FILES.get("teacher_files")
        if data["total_points"]:
            updateassignment.total_points = data["total_points"]
        updateassignment.save()
        return Response(
            {"message": "Assignment updated successfully"},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_submission_of_a_student_for_an_assignment(request, a_id, s_id):
    data = request.data
    print(data)
    try:
        updateassignment = Submit_Assignments.objects.get(
            assignment=a_id, student=s_id
        )
        print("here")
        if data["obtain_points"]:
            updateassignment.obtain_points = data["obtain_points"]
            updateassignment.marked = True
            updateassignment.save()

        return Response(
            {"message": "Submission marked successfully"},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_assignment(request, pk):
    try:
        deleteassignment = Give_Assignments.objects.get(id=pk)
        deleteassignment.delete()
        return Response(
            {"message": "Assignment deleted successfully"},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_assignments_for_a_student(request, c_id):
    showassignment = Give_Assignments.objects.filter(classes=c_id)
    serializer = Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_post_due_assignments_for_a_student(request, c_id):
    try:

        print(datetime.month())
        show_post_due_assignments = Give_Assignments.objects.filter(
            classes=c_id, due_date__lte=datetime.now()
        )
        serializer = Give_AssignmentsSerializer(show_post_due_assignments, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def calendar_view_for_student_for_month(request, c_id, month_id, year_id):
    try:
        show_post_due_assignments = Give_Assignments.objects.filter(
            classes=c_id, due_date__month=month_id, due_date__year=year_id
        )
        serializer = Give_AssignmentsSerializer(show_post_due_assignments, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_assignments_for_all_class_given_to_specific_student(request, s_id):
    showassignment = Give_Assignments.objects.filter(classes__student=s_id)
    serializer = Calendar_Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_all_assignments_for_all_class_given_to_specific_student_in_a_month(
    request, s_id, month_id, year_id
):
    showassignment = Give_Assignments.objects.filter(
        classes__student=s_id, due_date__month=month_id, due_date__year=year_id
    )
    serializer = Calendar_Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)
