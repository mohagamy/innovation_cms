import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import Information, InnovationCMSModel
from core.utlis import generate_file
from member.models import Member


def generate_proposal_document_file(self, filename):
    return generate_file(
        'grant_proposals/%s/docs' % str(self.grant_proposal.id), filename)


def generate_progress_report_file(self, filename):
    return generate_file(
        'grant_proposals/%s/reports' % str(self.grant_proposal.id), filename)


class GrantProposal(Information):

    submit_datetime = models.DateTimeField(default=datetime.datetime.now)

    authors = models.ManyToManyField(
        Member, verbose_name=_("Members"), blank=True)

    class Meta:
        verbose_name = _('GrantProposal')
        verbose_name_plural = _('GrantProposals')

    def __str__(self):
        return str(self.id)


class ProposalDocument(InnovationCMSModel):

    attachment = models.FileField(
        _("Proposal Document"), upload_to=generate_proposal_document_file)

    grant_proposal = models.ForeignKey(
        GrantProposal, verbose_name=_("Grant Proposal"),
        related_name='proposal_documents', error_messages={
            "blank": "Grant Proposal can not be empty.",
            "null": "Grant Proposal is a required field."})

    class Meta:
        verbose_name = _('ProposalDocument')
        verbose_name_plural = _('ProposalDocuments')

    def __str__(self):
        return str(self.id)


class ProgressReport(InnovationCMSModel):

    attachment = models.FileField(
        _("Progress Report"), upload_to=generate_progress_report_file)

    grant_proposal = models.ForeignKey(
        GrantProposal, verbose_name=_("Grant Proposal"),
        related_name='progress_reports', error_messages={
            "blank": "Grant Proposal can not be empty.",
            "null": "Grant Proposal is a required field."})

    class Meta:
        verbose_name = _('ProgressReport')
        verbose_name_plural = _('ProgressReports')

    def __str__(self):
        return str(self.id)
