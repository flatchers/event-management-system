from rest_framework import serializers

from models import Event, EventRegistration


class EventSerializer(serializers.Serializer):
    event_category = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    hold_date = serializers.DateTimeField()
    seats = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


