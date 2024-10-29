import uuid

from django.db import models

from system import settings


class Event(models.Model):
    class CategoryEvent(models.TextChoices):
        CONFERENCE = "Conference"
        WEBINAR = "Webinar"
        WORKSHOP = "Workshop"
        TRADE_SHOWS = "Trade shows"
        JOB_FAIRS = "Job fairs"
        NETWORKING = "Networking"
        MUSIC_FESTIVAL = "Music festival"

    event_category = models.CharField(max_length=255, choices=CategoryEvent.choices)
    name = models.CharField(max_length=255)
    description = models.TextField()
    hold_date = models.DateTimeField()
    seats = models.PositiveIntegerField
    price = models.DecimalField(max_digits=10, decimal_places=2)


class EventRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="registrations", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="registrations", on_delete=models.CASCADE)


class Payment:
    class Status(models.TextChoices):
        PENDING = "PENDING"
        PAID = "PAID"

    status = models.CharField(max_length=255, choices=Status.choices)
    registration_id = models.ForeignKey(EventRegistration,on_delete=models.CASCADE, related_name="payments")
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_url = models.URLField(max_length=200, null=True)
    money_to_pay = models.ManyToManyField(EventRegistration)
