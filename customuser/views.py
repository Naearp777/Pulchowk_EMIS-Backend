from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.


@api_view(['POST'])
def registerUser(request):
    
    data = request.data
    print(data)
    try:
        user = User.objects.create(
            password=make_password(data['password']),
            email=data['email'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            last_name=data['last_name'],
            roll_no=data['roll_no'],
            address=data['address'],
            gender=data['gender'],
            phone=data['phone'],
            dob=data['dob'],
            admin=data['admin'],
            student=data['student'],
            department=data['department'],
            staff=data['staff'],

        )
        
        user = User.objects.get(email=data['email'])
        user.images = request.FILES.get('images')
        user.save()
        serializer = UserSerializer(user, many=False)

        email_template = render_to_string('signup.html', {"first_name":serializer.data['first_name'],
                                           "password": serializer.data['password'], "email": serializer.data['email']})
        sign_up = EmailMultiAlternatives(
            "Account has been Created",
            "Account has been Created",
            settings.EMAIL_HOST_USER,
            [serializer.data['email']],
        )
        sign_up.attach_alternative(email_template, 'text/html')
        sign_up.send()

        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)