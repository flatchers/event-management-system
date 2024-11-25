from rest_framework import serializers

from models import Event, EventRegistration, Payment


class EventSerializer(serializers.Serializer):
    event_category = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    hold_date = serializers.DateTimeField()
    seats = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Event(**validated_data)

    def update(self, instance, validated_data):
        instance.event_category = validated_data.get("event_category", instance.event_category)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.hold_date = validated_data.get("hold_date", instance.hold_date)
        instance.seats = validated_data.get("seats", instance.seats)
        instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "status",
            "session_id",
            "session_url",
            "money_to_pay"
        )


class EventRegistrationSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer

    class Meta:
        model = EventRegistration
        fields = (
            "user",
            "event",
            "payment"
        )
