from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import serializers
from rest_framework import exceptions


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        print("username = ", username)

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "user is deactivated"
                    raise exceptions.ValidationError(msg)

            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Please provide username and password"
            raise exceptions.ValidationError(msg)

        print("serializer data = ", data)
        return data
