from rest_framework import serializers
from .models import Advisor, Call


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = (
            "id",
            "name",
        )


class BookCallSerializer(serializers.Serializer):
    booking_time = serializers.DateTimeField()


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"
