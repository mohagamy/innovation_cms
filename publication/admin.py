"""Publication custom admin."""
from django.contrib import admin
from django.contrib.admin.options import StackedInline
from django.contrib.admin import ModelAdmin

from core.utlis import admin_setup
from publication.models import PublicationType, Publication, PublicationFile


class StackedInlinePublicationFileAAdmin(StackedInline):
    model = PublicationFile
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('publication', 'attachment')
        }),
    )


class PublicationTypeAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'identifier', 'creation_datetime')
    list_display_links = ('id', )
    search_fields = ('name', 'identifier', )


class PublicationAdmin(ModelAdmin):
    list_display = (
        'id', 'title', 'creation_datetime', 'journal', '_type',
        'book_title', 'year', 'volume', 'number', 'start_page', 'end_page',
        'publisher', 'institution', 'address', 'note')
    list_display_links = ('id', )
    search_fields = ('title', )
    inlines = [StackedInlinePublicationFileAAdmin]


class PublicationFileAdmin(ModelAdmin):

    list_display = (
        'id', 'attachment', 'publication', 'creation_datetime')
    list_display_links = ('id', )

admin_setup.register(PublicationType, PublicationTypeAdmin)
admin.site.register(Publication, PublicationAdmin)
