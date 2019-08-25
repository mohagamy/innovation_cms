"""Recruitment custom admin."""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from recruitment.models import Recruitment


class RecruitmentAdmin(ModelAdmin):
    list_display = (
        'id', 'position', 'program', 'creation_datetime', 'start_datetime',
        'job_description')
    list_display_links = ('id', )

admin.site.register(Recruitment, RecruitmentAdmin)
