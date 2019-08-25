"""Equipment custom admin."""
from django.contrib import admin
from django.contrib.admin.options import StackedInline
from django.contrib.admin import ModelAdmin

from equipment.models import (
    Equipment, EquipmentQuote, EquipmentMaintenanceDocument, EquipmentManual,
    EquipmentLiciense, EquipmentDataSheet, EquipmentDocumentation,
    EquipmentFinancialDocument, EquipmentReceipt)


class StackedInlineEquipmentQuoteAdmin(StackedInline):
    model = EquipmentQuote
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentMaintenanceDocumentAdmin(StackedInline):
    model = EquipmentMaintenanceDocument
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentManualAdmin(StackedInline):
    model = EquipmentManual
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentDocumentationAdmin(StackedInline):
    model = EquipmentDocumentation
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentLicienseAdmin(StackedInline):
    model = EquipmentLiciense
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentDataSheetAdmin(StackedInline):
    model = EquipmentDataSheet
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentFinancialDocumentAdmin(StackedInline):
    model = EquipmentFinancialDocument
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class StackedInlineEquipmentReceiptAdmin(StackedInline):
    model = EquipmentReceipt
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('attachment', 'equipment')
        }),
    )


class EquipmentAdmin(ModelAdmin):
    list_display = (
        'id', 'name', 'company', 'creation_datetime', 'address',
        'description', 'cost', 'contact_person', 'receive_datetime',
        'start_datetime', 'end_datetime')
    list_display_links = ('id', )
    inlines = [
        StackedInlineEquipmentQuoteAdmin,
        StackedInlineEquipmentMaintenanceDocumentAdmin,
        StackedInlineEquipmentManualAdmin,
        StackedInlineEquipmentDocumentationAdmin,
        StackedInlineEquipmentLicienseAdmin,
        StackedInlineEquipmentDataSheetAdmin,
        StackedInlineEquipmentFinancialDocumentAdmin,
        StackedInlineEquipmentReceiptAdmin]


class EquipmentQuoteAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentMaintenanceDocumentAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentManualAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentDocumentationAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentLicienseAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentDataSheetAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentFinancialDocumentAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )


class EquipmentReceiptAdmin(ModelAdmin):
    list_display = (
        'id', 'attachment', 'equipment', 'creation_datetime')
    list_display_links = ('id', )

admin.site.register(Equipment, EquipmentAdmin)
