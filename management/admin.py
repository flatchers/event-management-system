from django.contrib import admin

from management.models import Event, EventRegistration


class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "event_category", "display_price", "display_hold_date_and_utc_time"]
    list_filter = ["name", "event_category", "price"]
    empty_value_display = "-not specified-"

    @admin.display(empty_value="soon")
    def display_hold_date_and_utc_time(self, obj):
        return obj.hold_date

    @admin.display(empty_value="free")
    def display_price(self, obj):
        return obj.price


class EventRegistrationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
