from django.contrib import admin

# Register your models here.
from base.models import Country, City, State

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
