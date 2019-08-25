import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import InnovationCMSModel, Type
from core.utlis import generate_file
from location.models import Location
from member.models import Member


def generate_document_file(self, filename):
    return generate_file(
        'events/%s/documents' % str(self.event.id), filename)


def generate_event_photo(self, filename):
    return generate_file(
        'events/%s/photos' % str(self.event.id), filename)


class EventType(Type):

    class Meta:
        verbose_name = _('EventType')
        verbose_name_plural = _('EventTypes')

    def __str__(self):
        return self.identifier


class Event(InnovationCMSModel):

    title = models.CharField(
        _('Title'), max_length=255,
        error_messages={
            "max_length": "Title must be less than 255 characters.",
            "blank": "Title can not be empty.",
            "null": "Title is a required field."})

    description = models.TextField(
        _('Description'), error_messages={
            "blank": "description can not be empty.",
            "null": "description is a required field."})

    start_datetime = models.DateTimeField(
        _("Start Date"), default=datetime.datetime.now, error_messages={
            "blank": "Start Date can not be empty.",
            "null": "Start Date is a required field."})

    end_datetime = models.DateTimeField(
        _("End Date"), default=datetime.datetime.now, error_messages={
            "blank": "End Date can not be empty.",
            "null": "End Date is a required field."})

    _type = models.ForeignKey(
        EventType, related_name='events', error_messages={
            "blank": "EventType can not be empty.",
            "null": "EventType is a required field."})

    location = models.ForeignKey(
        Location, related_name='events', error_messages={
            "blank": "Location can not be empty.",
            "null": "Location is a required field."})

    members = models.ManyToManyField(
        Member, through='EventMember', related_name='events',
        through_fields=('event', 'member'))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return str(self.id)


class EventMember(InnovationCMSModel):

    member = models.ForeignKey(
        Member, related_name='event_members', error_messages={
            "blank": "Member can not be empty.",
            "null": "Member is a required field."})

    event = models.ForeignKey(
        Event, related_name='event_members', error_messages={
            "blank": "Event can not be empty.",
            "null": "Event is a required field."})

    class Meta:
        verbose_name = _('EventMember')
        verbose_name_plural = _('EventMembers')

    def __str__(self):
        return str(self.id)


class EventDocument(InnovationCMSModel):

    attachment = models.FileField(
        _("Event Document"), upload_to=generate_document_file)

    event = models.ForeignKey(
        Event, verbose_name=_("Event"), error_messages={
            "blank": "Event can not be empty.",
            "null": "Event is a required field."})

    class Meta:
        verbose_name = _('EventDocument')
        verbose_name_plural = _('EventDocuments')

    def __str__(self):
        return str(self.id)


class EventPhoto(InnovationCMSModel):

    attachment = models.ImageField(
        _("Event Photo"), upload_to=generate_event_photo)

    event = models.ForeignKey(
        Event, verbose_name=_("Event"), error_messages={
            "blank": "Event can not be empty.",
            "null": "Event is a required field."})

    class Meta:
        verbose_name = _('EventPhoto')
        verbose_name_plural = _('EventPhotos')

    def __str__(self):
        return str(self.id)
