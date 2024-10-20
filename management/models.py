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

    event_category = models.CharField(max_length=255, choices=CategoryEvent)
    name = models.CharField(max_length=255)
    description = models.TextField()
    hold_date = models.DateTimeField()
    seats = models.PositiveIntegerField
    price = models.DecimalField(max_digits=10, decimal_places=2)


class EventRegistration:
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="registrations", on_delete=models.CASCADE)
