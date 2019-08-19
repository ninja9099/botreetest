from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Base(models.Model):
    created_ts = models.DateTimeField(_("Created Date"), auto_now_add=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s_created_related', null=True, blank=True,
                                   on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s_updated_related', null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Country(Base):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "bmc_country"
        verbose_name_plural = "Countries"
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.name


class State(Base):
    country = models.ForeignKey(Country, related_name='state_set', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "bmc_state"
        verbose_name_plural = "States"
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name


class City(Base):
    state = models.ForeignKey(State, related_name='city_set', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "bmc_city"
        verbose_name_plural = "Cities"
        unique_together = ('name', 'state')

    def __str__(self):
        return self.name