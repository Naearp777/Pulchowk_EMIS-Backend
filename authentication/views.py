from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializerWithToken
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from customuser.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.


@api_view(["POST"])
def get_self_role(request):
    data = request.data
    access_token_object = AccessToken(data["access"])
    user_id = access_token_object["user_id"]
    user = User.objects.get(id=user_id)

    if user.admin:
        role = "ADMIN"
        return Response(role, status=status.HTTP_200_OK)
    elif user.department:
        role = "DEPT_ADMIN"
        return Response(role, status=status.HTTP_200_OK)
    elif user.staff:
        role = "TEACHER"
        return Response(role, status=status.HTTP_200_OK)
    elif user.student:
        role = "STUDENT"
        return Response(role, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
