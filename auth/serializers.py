from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150, required=True)
    # unique validation for email
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True)


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(required=True)
