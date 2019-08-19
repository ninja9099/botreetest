from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from base.models import Base

User = settings.AUTH_USER_MODEL


class CleanerBookings(Base):
    cleaner = models.ForeignKey(User, related_name='cleaner_set',  on_delete=models.CASCADE)
    customer = models.ForeignKey(User, related_name='customer_set', on_delete=models.CASCADE)
    booking_starttime = models.DateTimeField()
    booking_endtime = models.DateTimeField()

    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')

    def __str__(self):
        return "{}{}{}".format(self.cleaner, self.booking_starttime, self.booking_endtime)