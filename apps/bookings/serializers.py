from rest_framework import serializers

from apps.bookings.models import CleanerBookings


class CleanerBookingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CleanerBookings
        fields = (
            "id",
            "cleaner",
            "customer",
            "booking_starttime",
            "booking_endtime",
        )