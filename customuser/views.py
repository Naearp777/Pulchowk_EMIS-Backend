from batch.models import batch
from department.models import department
from section.models import section
from .serializers import UserSerializer,UserExportSerializer
from .models import User,ExcelFileUpload
from student.models import student_info
from teacher.models import Teachers_info
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.crypto import get_random_string
import csv
import pandas as pd
from rest_framework.views import APIView
from django.conf import settings
# Create your views here.


@api_view(['POST'])
def registerUser(request):
    
    data = request.data
    try:
        user = User.objects.create(
            password=get_random_string(length=7),
            email=data['email'],
            first_name=data['first_name'],
            middle_name=data['middle_name'],
            last_name=data['last_name'],
            address=data['address'],
            gender=data['gender'],
            phone=data['phone'],
            dob=data['dob'],
            admin=data['admin'],
            student=data['student'],
            department=data['department'],
            staff=data['staff'],
            password_changed=data['password_changed'],

        )
        
        user = User.objects.get(email=data['email'])
        user.images = request.FILES.get('images')
        user.save()
        serializer = UserSerializer(user, many=False)
        if(serializer.data['student']==True):
            student_info.objects.create(
                student= User.objects.get(email=data['email']),
                rollno=data['roll_no'],
                department=department.objects.get(name=data['department_name']),
                batch=batch.objects.get(name=data['batch']),
                section=section.objects.get(name=data['section']),
            )
        if(serializer.data['staff']==True):
                Teachers_info.objects.create(
                department=department.objects.get(name=data['department_name']),
            )

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
        user.password=make_password(user.password)
        user.save()
        

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)




class ExportUserCSV(APIView):
    
    def get(self , request):
        users  = User.objects.all()
        serializer = UserExportSerializer(users, many=True)
        df  = pd.DataFrame(serializer.data)
        df.to_csv('media/excel/export.csv', index=False)
        # print(df)
        return Response(serializer.data)

class ImportUserCSV(APIView):
    def post(self,request):
        
        excel_upload = ExcelFileUpload.objects.create()
        excel_upload.excel_file = request.FILES.get('files')
        df = pd.read_csv(f"{settings.BASE_DIR}/media/excel/{excel_upload.excel_file}")
        print(df.values.tolist())
        for user in df.values.tolist() :
            User.objects.create(
            password    =get_random_string(length=7),
            email       =user[0],
            first_name  =user[1],
            middle_name =user[2],
            last_name   =user[3],
            address     =user[5],
            gender      =user[6],
            phone       =user[7],
            dob         =user[8],
            student     =user[9],
            staff       =user[10],
            department  =user[11],
            admin       =user[12],
            )
            new_user = User.objects.get(email=user[0])
            serializer = UserSerializer(new_user, many=False)
            
            if(serializer.data['student']==True):
                student_info.objects.create(
                student= User.objects.get(email=user[0]),
                rollno=user[4],
                department=department.objects.get(department_name=user[13]),
                batch=batch.objects.get(batch=user[14]),
                section=section.objects.get(section=user[15]),
            )
            if(serializer.data['staff']==True):
                Teachers_info.objects.create(
                department=department.objects.get(department_name=user[13]),
               
            )
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
            new_user.password=make_password(new_user.password)
            new_user.save()
        return Response(status=status.HTTP_201_CREATED)
     