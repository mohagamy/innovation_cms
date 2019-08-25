"""Project core models."""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from audit_log.models import AuthStampedModel

from django.db.models.signals import pre_delete, post_delete


class InnovationCMSQuerySet(models.query.QuerySet):
    """ This class overrides delete, hard_delete, undo_delete.
        Each Queryset should have one or more objects of InnovationCMS
        objects.Each Assessment Object has a property delete, hard_delete,
        undo_delete. This class overrides the QuerySet to enable usage of
        those property on Queryset.
    """
    def delete(self):
        for innovation_cms_object in self:
            innovation_cms_object.delete()

    def hard_delete(self):
        for innovation_cms_object in self:
            innovation_cms_object.hard_delete()

    def undo_delete(self):
        for innovation_cms_object in self:
            innovation_cms_object.undo_delete()


class InnovationCMSManager(models.Manager):
    def get_queryset(self):
        return InnovationCMSQuerySet(self.model).filter(
            is_deleted=False)

    def custom_queryset(self, *filterList, **filters):
        return InnovationCMSQuerySet(self.model).filter(
            *filterList, **filters)

    def hard_delete(self):
        return InnovationCMSQuerySet(self.model).hard_delete()

    def delete(self):
        return InnovationCMSQuerySet(self.model).delete()


class InnovationCMSModel(AuthStampedModel):
    """ Adding support for creation_date and last_modified
     in inhiriting models
     """
    creation_datetime = models.DateTimeField(editable=False, auto_now_add=True)
    last_modified_datetime = models.DateTimeField(
        editable=False, auto_now=True)
    is_deleted = models.BooleanField(
        editable=False, default=False, db_index=True)

    objects = InnovationCMSManager()

    def save(self, **kwargs):
        """Override save function to validate on model's fields."""
        exclude = []
        if type(self).__name__ == 'Member':
            exclude = ['password']
        self.full_clean(exclude=exclude)
        return super(InnovationCMSModel, self).save(**kwargs)

    def delete(self):
        pre_delete.send(sender=self.__class__, instance=self)
        self.is_deleted = True
        self.save()
        post_delete.send(sender=self.__class__, instance=self)

    def hard_delete(self):
        super(InnovationCMSModel, self).delete()

    def undo_delete(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Type(InnovationCMSModel):

    name = models.CharField(
        _('Name'), max_length=255,
        error_messages={
            "max_length": "Name must be less than 255 characters.",
            "blank": "Name can not be empty.",
            "null": "Name is a required field."})

    identifier = models.CharField(
        _('Identfier'), max_length=30,
        error_messages={
            "max_length": "Identfier must be less than 30 characters.",
            "blank": "Identfier can not be empty.",
            "null": "Identfier is a required field."})

    class Meta:
        abstract = True


class Information(InnovationCMSModel):

    title = models.CharField(
        _('Title'), max_length=30,
        error_messages={
            "max_length": "Title must be less than 30 characters.",
            "blank": "Title can not be empty.",
            "null": "Title is a required field."})

    description = models.TextField(
        _('Description'), error_messages={
            "blank": "Description can not be empty.",
            "null": "Description is a required field."})

    objective = models.TextField(
        _('Objective'), null=True, error_messages={
            "blank": "Objective can not be empty."})

    update = models.TextField(
        _('Update'), null=True, error_messages={
            "blank": "Update can not be empty."})

    class Meta:
        abstract = True
