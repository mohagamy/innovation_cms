"""Location custom admin."""
from django.contrib.admin import ModelAdmin

from core.utlis import admin_setup
from location.models import Location


class LocationAdmin(ModelAdmin):
    list_display = (
        'id', 'city', 'street', 'creation_datetime', 'room', 'number')
    list_display_links = ('id', )
    search_fields = ('city', 'street', 'room', 'number')

admin_setup.register(Location, LocationAdmin)
