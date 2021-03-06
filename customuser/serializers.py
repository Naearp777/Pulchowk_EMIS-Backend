from dataclasses import field
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "id",
            "last_login",
            "images",
            "student",
            "staff",
            "admin",
            "department",
            "password_changed",
        ]


class UserSerializer_std(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "last_login"]


class UserExportSerializer_assessment(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "email",
            "password",
            "id",
            "last_login",
            "images",
            "student",
            "staff",
            "admin",
            "department",
            "password_changed",
            "phone",
            "dob",
            "address",
            "middle_name",
            "roll_no",
            "gender",
        ]
