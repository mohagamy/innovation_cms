"""Proposal custom admin."""
from django.contrib import admin
from django.contrib.admin.options import StackedInline
from django.contrib.admin import ModelAdmin

from proposal.models import ProposalDocument, ProgressReport, GrantProposal


class StackedInlineProposalDocumentAdmin(StackedInline):
    model = ProposalDocument
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('grant_proposal', 'attachment')
        }),
    )


class StackedInlineProgressReportAdmin(StackedInline):
    model = ProgressReport
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('grant_proposal', 'attachment')
        }),
    )


class GrantProposalAdmin(ModelAdmin):
    list_display = (
        'id', 'submit_datetime', 'creation_datetime', 'title',
        'description', 'objective', 'update')
    list_display_links = ('id', )
    inlines = [StackedInlineProgressReportAdmin,
               StackedInlineProposalDocumentAdmin]


class ProposalDocumentAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'grant_proposal', 'creation_datetime')
    list_display_links = ('id', )


class ProgressReportAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'grant_proposal', 'creation_datetime')
    list_display_links = ('id', )


admin.site.register(GrantProposal, GrantProposalAdmin)
admin.site.register(ProgressReport, ProgressReportAdmin)
#admin.site.register(ProposalDocument, ProposalDocumentAdmin)
