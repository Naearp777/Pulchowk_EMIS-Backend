
from assignments.models import Give_Assignments,Submit_Assignments
from customuser.models import User
from classes.models import classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from .serializers import Give_AssignmentsSerializer,Submit_AssignmentsSerializer
from rest_framework.decorators import api_view
from notice.models import notice
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_assignment(request,c_id,t_id):
    data=request.data
    try:
        Give_Assignments.objects.create(
        classes=classes.objects.get(id=c_id),
        teacher=User.objects.get(id=t_id),
        title=data['title'],
        description=data['description'],
        due_date=data['due_date'],
        created_at=data['created_at'],
        updated_at=data['updated_at'],
        teacher_files=request.FILES.get('teacher_files'),
        )
        notice.objects.create(
            title=data['title'],
            content=data['description'],
            created_at=data['created_at'],
            publish_to=classes.objects.get(id=c_id),
            publish_by=User.objects.get(id=t_id).first_name+" "+User.objects.get(id=t_id).last_name,
        )
        return Response ({"message":"Assignment created successfully"},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response ({"message": str(e) },status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_assignment(request,a_id,s_id):
    data=request.data
    try:
        Submit_Assignments.objects.create(
        student=User.objects.get(id=s_id),
        assignment=Give_Assignments.objects.get(id=a_id),
        student_files=request.FILES.get('student_files'),
        )
        return Response ({"message":"Assignment submitted successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response ({"message":"Assignment not submitted"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_assignment(request,pk):
    showassignment=Give_Assignments.objects.get(id=pk)
    serializer = Give_AssignmentsSerializer(showassignment, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_assignment_given_by_teacher_in_specific_class(request,t_id,c_id):
    showassignment=Give_Assignments.objects.filter(teacher=t_id,classes=c_id)
    serializer = Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_submitted_assignments_for_an_assignment(request,a_id):
    showassignment=Submit_Assignments.objects.filter(assignment=a_id)
    serializer = Submit_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_submitted_assignments_for_a_student(request,s_id):
    showassignment=Submit_Assignments.objects.filter(student=s_id)
    serializer = Submit_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_submitted_assignments_for_a_student_in_a_class(request,s_id,c_id): 
    showassignment=Submit_Assignments.objects.filter(student=s_id,assignment__classes=c_id)
    serializer = Submit_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_assignment(request,pk):
    data=request.data
    try:
        updateassignment=Give_Assignments.objects.get(id=pk)
        updateassignment.title=data['title']
        updateassignment.description=data['description']
        updateassignment.due_date=data['due_date']
        updateassignment.created_at=data['created_at']
        updateassignment.updated_at=data['updated_at']
        updateassignment.teacher_files=request.FILES.get('teacher_files')
        updateassignment.save()
        return Response ({"message":"Assignment updated successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response ({"message":"Assignment not updated"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_assignment(request,pk):
    try:
        deleteassignment=Give_Assignments.objects.get(id=pk)
        deleteassignment.delete()
        return Response ({"message":"Assignment deleted successfully"},status=status.HTTP_201_CREATED)
    except:
        return Response ({"message":"Assignment not deleted"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_assignments_for_a_student(request,s_id):
    showassignment=Give_Assignments.objects.filter(student=s_id)
    serializer = Give_AssignmentsSerializer(showassignment, many=True)
    return Response(serializer.data)

