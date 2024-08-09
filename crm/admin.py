from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# admin.site.register(CompanyFullKYC)


@admin.register(CompanyFullKYC)
class CompanyFullKYCAdmin(ImportExportModelAdmin):
    list_display = ['company_name',
                    'updated',
                    'created']

# admin.site.register(Affiliations)


@admin.register(Affiliations)
class AffiliationsAdmin(ImportExportModelAdmin):
    list_display = ['id']

# admin.site.register(OfficeRole)


@admin.register(OfficeRole)
class OfficeRoleAdmin(ImportExportModelAdmin):
    list_display = ['id']

# admin.site.register(BackendStaff)


@admin.register(BackendStaff)
class BackendStaffAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']


# admin.site.register(Location)
@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']


# admin.site.register(SubLocation)
@admin.register(SubLocation)
class SubLocationAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']


# admin.site.register(PaymentStatus)
@admin.register(PaymentStatus)
class PaymentStatusAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']


# admin.site.register(ArivalTable)
@admin.register(ArivalTable)
class ArivalTableAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']

# admin.site.register(Currency)


@admin.register(Currency)
class CurrencyAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']


# admin.site.register(Gurantee)
@admin.register(Gurantee)
class GuranteeAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']

# admin.site.register(StaffDetails)


@admin.register(StaffDetails)
class StaffDetailsAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'updated',
                    'created']

# FocusArea


@admin.register(FocusArea)
class FocusAreaAdmin(ImportExportModelAdmin):
    list_display = ['id', "focus_area",
                    'updated',
                    'created']

# CategoryClients


@admin.register(CategoryClients)
class CategoryClientsAdmin(ImportExportModelAdmin):
    list_display = ['id', "category_clients",
                    'updated',
                    'created']

# ContactTable


@admin.register(ContactTable)
class ContacttableAdmin(ImportExportModelAdmin):
    list_display = ['company_name', 'person_name', 'person_phone',
                    'person_email',
                    'contact_city',
                    'updated',
                    'created']

# State


@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'state_name', 'state_code', 'gstin_code')

# NewCompanyRegistration


@admin.register(NewCompanyRegistration)
class NewCompanyRegistrationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'company_name', 'company_city',
                    'person_name', 'person_phone')


# CompanyKYCDetails
@admin.register(CompanyKYCDetails)
class CompanyKYCDetailsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'company_kyc', 'company_branch')


# Feedbacks
@admin.register(Feedback)
class FeedbackAdmin(ImportExportModelAdmin):
    list_display = ('id', 'creator', 'suggestion_title',
                    'description',
                    'suport_file')
