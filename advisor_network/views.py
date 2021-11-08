from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .models import Advisor, Call
from .serializers import AdvisorSerializer, BookCallSerializer, CallSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(["POST"])
def add_advisor(request):
    serializer = AdvisorSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data={}, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()

    return Response(data=None, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def list_advisors(request, user_id):
    advisors = []
    user = User.objects.get(pk=user_id)
    if user:
        advisors = user.advisor_set.distinct().all()
        serializer = AdvisorSerializer(advisors, many=True)
        advisors = serializer.data

    return Response(
        data=advisors,
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def book_call(request, user_id, advisor_id):
    serializer = BookCallSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(pk=user_id)
    advisor = Advisor.objects.get(pk=advisor_id)
    if not user or not advisor:
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

    call = Call(
        user=User.objects.get(pk=user_id),
        advisor=Advisor.objects.get(pk=advisor_id),
        booking_time=serializer.validated_data["booking_time"],
    )
    call.save()

    return Response(data=None, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def list_booked_calls(request, user_id):
    user = User.objects.get(pk=user_id)

    calls = Call.objects.filter(user=user).all()
    serializer = CallSerializer(calls, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
