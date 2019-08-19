from django.contrib import admin

# Register your models here.
from apps.bookings.models import CleanerBookings

admin.site.register(CleanerBookings)