import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import Information
from member.models import Member


class Project(Information):

    start_datetime = models.DateTimeField(default=datetime.datetime.now)

    end_datetime = models.DateTimeField(default=datetime.datetime.now)

    member = models.ForeignKey(
        Member, verbose_name=_("Member"), related_name='projects', null=True,
        error_messages={"blank": "Member can not be empty."})

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return str(self.id)


class Idea(Information):

    reference = models.TextField(
        _('Reference'), null=True, blank=True)

    member = models.ForeignKey(
        Member, verbose_name=_("Member"), related_name='ideas', null=True,
        blank=True)

    class Meta:
        verbose_name = _('Idea')
        verbose_name_plural = _('Ideas')

    def __str__(self):
        return str(self.id)
