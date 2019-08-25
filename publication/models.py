from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import InnovationCMSModel, Type
from core.utlis import generate_file
from member.models import Member


def generate_paper_file(self, filename):
    return generate_file(
        'publications/%s/files' % str(self.publication.id), filename)


class PublicationType(Type):

    class Meta:
        verbose_name = _('PublicationType')
        verbose_name_plural = _('PublicationTypes')

    def __str__(self):
        return self.identifier


class PublicationAuthor(InnovationCMSModel):

    name = models.CharField(
        max_length=100, unique=True,
        error_messages={
            'unique': "This Username has already been registered.",
            "max_length": "Username must be less than 30 characters.",
            "blank": "Username can not be empty.",
            "null": "Username is a required field."})

    class Meta:
        verbose_name = _('PublicationAuthor')
        verbose_name_plural = _('PublicationAuthors')

    def __str__(self):
        return self.name


class Publication(InnovationCMSModel):

    title = models.CharField(
        _('Title'), max_length=500,
        error_messages={
            "max_length": "Title must be less than 30 characters.",
            "blank": "Title can not be empty.",
            "null": "Title is a required field."})

    journal = models.TextField(
        _('Journal'), error_messages={
            "blank": "Journal can not be empty.",
            "null": "Journal is a required field."})

    _type = models.ForeignKey(
        PublicationType, related_name='events', null=True, blank=True)

    authors = models.ManyToManyField(
        PublicationAuthor, verbose_name=_("Authors"), blank=True)

    book_title = models.CharField(
        _('Book Title'), max_length=100, null=True, blank=True,
        error_messages={
            "max_length": "Book Title must be less than 100 characters."})

    year = models.IntegerField(
        _("Publication Year"), null=True, blank=True)

    volume = models.IntegerField(
        _("Publication Volume"), null=True, blank=True)

    number = models.IntegerField(
        _("Publication Number"), null=True, blank=True)

    start_page = models.IntegerField(
        _("Start Page"), null=True, blank=True)

    end_page = models.IntegerField(
        _("End Page"), null=True, blank=True)

    publisher = models.CharField(
        _('Publisher'), null=True, max_length=100, blank=True,
        error_messages={
            "max_length": "Publisher must be less than 100 characters."})

    institution = models.CharField(
        _('Institution'), max_length=100, null=True, blank=True,
        error_messages={
            "max_length": "Institution must be less than 100 characters."})

    address = models.CharField(
        _('Address'), max_length=255, null=True, blank=True,
        error_messages={
            "max_length": "Address must be less than 255 characters."})

    note = models.TextField(
        _('Note'), null=True, blank=True)

    abstract = models.TextField(_('Paper Abstract'), null=True, blank=True)

    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')

    def __str__(self):
        return str(self.id)


class PublicationMember(InnovationCMSModel):

    member = models.ForeignKey(
        Member, related_name='publication_members',
        error_messages={
            "blank": "Member can not be empty.",
            "null": "Member is a required field."})

    publication = models.ForeignKey(
        Publication, related_name='publication_members',
        error_messages={
            "blank": "Publication can not be empty.",
            "null": "Publication is a required field."})

    class Meta:
        verbose_name = _('PublicationMember')
        verbose_name_plural = _('PublicationMembers')

    def __str__(self):
        return str(self.id)


class PublicationFile(InnovationCMSModel):

    attachment = models.FileField(
        _("Publication File"), upload_to=generate_paper_file)

    publication = models.ForeignKey(
        Publication, verbose_name=_("Publication"),
        related_name='publication_files', error_messages={
            "blank": "Publication can not be empty.",
            "null": "Publication is a required field."})

    class Meta:
        verbose_name = _('PublicationFile')
        verbose_name_plural = _('PublicationFiles')

    def __str__(self):
        return str(self.id)
