import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import InnovationCMSModel
from core.utlis import generate_file


def generate_quote_file(self, filename):
    return generate_file(
        'equipments/%s/equipment_quotes' % str(self.equipment.id), filename)


def generate_maintenance_doc_file(self, filename):
    return generate_file(
        'equipments/%s/maintenance_docs' % str(self.equipment.id), filename)


def generate_manual_file(self, filename):
    return generate_file(
        'equipments/%s/mannuals' % str(self.equipment.id), filename)


def generate_license_file(self, filename):
    return generate_file(
        'equipments/%s/licienses' % str(self.equipment.id), filename)


def generate_data_sheet_file(self, filename):
    return generate_file(
        'equipments/%s/data_sheets' % str(self.equipment.id), filename)


def generate_documentation_file(self, filename):
    return generate_file(
        'equipments/%s/docs' % str(self.equipment.id), filename)


def generate_financial_document_file(self, filename):
    return generate_file(
        'equipments/%s/financial_docs' % str(self.equipment.id), filename)


def generate_receipt_file(self, filename):
    return generate_file(
        'equipments/%s/receipts' % str(self.equipment.id), filename)


class Equipment(InnovationCMSModel):

    name = models.CharField(
        _('Name'), max_length=255,
        error_messages={
            "max_length": "Name must be less than 255 characters.",
            "blank": "Name can not be empty.",
            "null": "Name is a required field."})

    company = models.CharField(
        _('Company'), max_length=255,
        error_messages={
            "max_length": "Company must be less than 255 characters.",
            "blank": "Company can not be empty.",
            "null": "Company is a required field."})

    address = models.CharField(
        _('Address'), max_length=255,
        error_messages={
            "max_length": "Address must be less than 255 characters.",
            "blank": "Address can not be empty.",
            "null": "Address is a required field."})

    description = models.TextField(
        _('Description'), error_messages={
            "blank": "Description can not be empty.",
            "null": "Description is a required field."})

    cost = models.IntegerField(
        _("Cost"), error_messages={
            "blank": "Cost can not be empty.",
            "null": "Cost is a required field."})

    contact_person = models.CharField(
        _('Contact Person'), max_length=255,
        error_messages={
            "max_length": "Contact Person must be less than 255 characters.",
            "blank": "Contact Person can not be empty.",
            "null": "Contact Person is a required field."})

    receive_datetime = models.DateTimeField(default=datetime.datetime.now)

    start_datetime = models.DateTimeField(default=datetime.datetime.now)

    end_datetime = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipments')

    def __str__(self):
        return str(self.id)


class EquipmentQuote(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Quote File"), upload_to=generate_quote_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_quotes', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('Quote')
        verbose_name_plural = _('Quotes')

    def __str__(self):
        return str(self.id)


class EquipmentMaintenanceDocument(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Maintenance Document"),
        upload_to=generate_maintenance_doc_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_maintenance_docs', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('MaintenanceDocument')
        verbose_name_plural = _('MaintenanceDocuments')

    def __str__(self):
        return str(self.id)


class EquipmentManual(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Manual"), upload_to=generate_manual_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_mannuals', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('Manual')
        verbose_name_plural = _('Manuals')

    def __str__(self):
        return str(self.id)


class EquipmentLiciense(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment License"), upload_to=generate_license_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_licenses', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('Liciense')
        verbose_name_plural = _('Licienses')

    def __str__(self):
        return str(self.id)


class EquipmentDataSheet(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Data Sheet"), upload_to=generate_data_sheet_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_data_sheets', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('DataSheet')
        verbose_name_plural = _('DataSheets')

    def __str__(self):
        return str(self.id)


class EquipmentDocumentation(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Docummentation"), upload_to=generate_documentation_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_documentations', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('Documentation')
        verbose_name_plural = _('Documentations')

    def __str__(self):
        return str(self.id)


class EquipmentFinancialDocument(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Financial Document"),
        upload_to=generate_financial_document_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_financial_documents', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('FinancialDocument')
        verbose_name_plural = _('FinancialDocuments')

    def __str__(self):
        return str(self.id)


class EquipmentReceipt(InnovationCMSModel):

    attachment = models.FileField(
        _("Equipment Receipt"), upload_to=generate_receipt_file)

    equipment = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"),
        related_name='equipment_receipts', error_messages={
            "blank": "Equipment can not be empty.",
            "null": "Equipment is a required field."})

    class Meta:
        verbose_name = _('Receipt')
        verbose_name_plural = _('Receipts')

    def __str__(self):
        return str(self.id)
