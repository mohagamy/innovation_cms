"""Project custom admin."""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from project.models import Project, Idea


class ProjectAdmin(ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'objective', 'update',
        'creation_datetime', 'start_datetime', 'end_datetime', 'member')
    list_display_links = ('id', )
    search_fields = ('title', 'description', )


class IdeaAdmin(ModelAdmin):
    list_display = (
        'id', 'title', 'description', 'objective', 'update',
        'creation_datetime', 'update', 'member')
    list_display_links = ('id', )
    search_fields = ('title', 'description', )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Idea, IdeaAdmin)
