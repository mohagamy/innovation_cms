from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import InnovationCMSModel


class Location(InnovationCMSModel):

    city = models.CharField(
        _('City'), max_length=30, null=True, blank=True,
        error_messages={
            "max_length": "City must be less than 30 characters."})

    street = models.CharField(
        _('Street'), max_length=30, null=True, blank=True,
        error_messages={
            "max_length": "Street must be less than 30 characters."})

    room = models.CharField(
        _('Room'), max_length=30, null=True, blank=True,
        error_messages={
            "max_length": "Room must be less than 30 characters."})

    number = models.CharField(
        _('Number'), max_length=30, null=True, blank=True,
        error_messages={
            "max_length": "Number must be less than 30 characters."})

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return 'city: %s | street: %s | room: %s | number: %s' % (
            self.city, self.street, self.room, self.number)
