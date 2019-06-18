from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.contrib.auth.models import User as UserModel

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer

from user_management.models import UserInfo


class UserLogin(APIView):
    def post(self, request):
        authentication_classes = (TokenAuthentication,)

        # <view logic>
        print("request = ", request)
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class UserSignUp(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):

        password = request.data["password"]
        email = request.data["username"]
        email = email.lower()
        username = email

        if UserModel.objects.filter(email=email):
            # Email address belongs to registered user
            msg = "Email address belongs to registered user"
            return Response(msg, status=400)

        elif UserModel.objects.filter(username=username):
            # Email address belongs to registered user
            msg = "username belongs to registered user"
            return Response(msg, status=400)

        else:
            newUser = UserModel(
                username=email, email=email, password=password, is_active=True
            )
            newUser.set_password(newUser.password)
            newUser.save()

            new_UserInfo = UserInfo(user=newUser)
            new_UserInfo.save()

            user = authenticate(username=username, password=password)
            if user:
                django_login(request, user)
            else:
                msg = "error"
                return Response(msg, status=400)

            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
