import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import InnovationCMSModel


class Recruitment(InnovationCMSModel):

    position = models.CharField(
        _('Position'), max_length=255,
        error_messages={
            "max_length": "Position must be less than 255 characters.",
            "blank": "Position can not be empty.",
            "null": "Position is a required field."})

    program = models.CharField(
        _('Company'), max_length=255,
        error_messages={
            "max_length": "Company must be less than 255 characters.",
            "blank": "Company can not be empty.",
            "null": "Company is a required field."})

    start_datetime = models.DateTimeField(default=datetime.datetime.now)

    job_description = models.TextField(
        _('Job Description'), error_messages={
            "blank": "Job Description can not be empty.",
            "null": "Job Description is a required field."})

    class Meta:
        verbose_name = _('Recruitment')
        verbose_name_plural = _('Recruitments')

    def __str__(self):
        return str(self.id)
