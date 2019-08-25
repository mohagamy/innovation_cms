"""Event custom admin."""
from django.contrib import admin
from django.contrib.admin.options import StackedInline
from django.contrib.admin import ModelAdmin

from core.utlis import admin_setup
from event.models import (
    EventType, Event, EventDocument, EventPhoto)


class StackedInlineEventDocumentAdmin(StackedInline):
    model = EventDocument
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('event', 'attachment')
        }),
    )


class StackedInlineEventPhotoAdmin(StackedInline):
    model = EventPhoto
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('event', 'attachment')
        }),
    )


class EventTypeAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'identifier', 'creation_datetime')
    list_display_links = ('id', )
    search_fields = ('name', 'identifier', )


class EventAdmin(ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'creation_datetime', 'start_datetime',
        'end_datetime', '_type', 'location')
    list_display_links = ('id', )
    search_fields = ('title', 'description', )
    inlines = [StackedInlineEventPhotoAdmin, StackedInlineEventDocumentAdmin]


class EventMemberAdmin(ModelAdmin):
    list_display = (
        'id', 'event', 'member', 'creation_datetime')
    list_display_links = ('id', )
    search_fields = ('event', 'member', )


class EventDocumentAdmin(ModelAdmin):
    list_display = (
        'id', 'event', 'attachment', 'creation_datetime')
    list_display_links = ('id', )


class EventPhotoAdmin(ModelAdmin):
    list_display = (
        'id', 'event', 'attachment', 'creation_datetime')
    list_display_links = ('id', )


admin.site.register(Event, EventAdmin)
admin_setup.register(EventType, EventTypeAdmin)
