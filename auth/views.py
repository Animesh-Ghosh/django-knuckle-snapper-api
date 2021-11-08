from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework.reverse import reverse
from django.db.models import Max
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data["email"].split("@")[0]
    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]
    split_name = serializer.validated_data["name"].split(" ")
    first_name = split_name[0]
    last_name = None
    if len(split_name) > 1:
        last_name = split_name[-1]

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    refresh = RefreshToken.for_user(user)

    return Response(
        data={
            "id": user.id,
            "access_token": str(refresh.access_token),
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def login(request):
    serializer = LoginUserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=serializer.validated_data["email"]).first()
    if user is None or not user.check_password(serializer.validated_data["password"]):
        return Response(
            data={"error": "Invalid Credentials!"}, status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(user)
    return Response(
        data={"id": user.id, "access_token": str(refresh.access_token)},
        status=status.HTTP_200_OK,
    )
