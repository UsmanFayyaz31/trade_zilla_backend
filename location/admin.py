from django.contrib import admin
from location.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')


# Register your models here.
admin.site.register(Location, LocationAdmin)
