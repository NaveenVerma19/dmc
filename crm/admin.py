from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# admin.site.register(CompanyFullKYC)


# @admin.register(CompanyFullKYC)
# class CompanyFullKYCAdmin(ImportExportModelAdmin):
#     list_display = ['company_name',
#                     'updated',
#                     'created']

# admin.site.register(Affiliations)

# State
@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ('state_name', 'id', 'state_code', 'gstin_code')


# admin.site.register(StaffDetails)

@admin.register(StaffDetails)
class StaffDetailsAdmin(ImportExportModelAdmin):
    list_display = ['username',
                    'id',
                    'user_full_name',
                    'email',
                    'updated',
                    'created']


# NewCompanyRegistration

@admin.register(NewCompanyRegistration)
class NewCompanyRegistrationAdmin(ImportExportModelAdmin):
    list_display = ( 'company_name',
                    'id',
                    'gst_number',
                    'company_city',
                    'person_name',
                    'person_phone',
                    'created')



# admin.site.register(OfficeRole)
@admin.register(OfficeRole)
class OfficeRoleAdmin(ImportExportModelAdmin):
    list_display = ['office_role', 'id']


# Affiliations
@admin.register(Affiliations)
class AffiliationsAdmin(ImportExportModelAdmin):
    list_display = ['affiliations','id']


# CompanyKYCDetails
@admin.register(CompanyKYCDetails)
class CompanyKYCDetailsAdmin(ImportExportModelAdmin):
    list_display = ('company_kyc',
                    'id',
                    'company_branch',
                    'gstin',
                    'company_city')


# FocusArea
@admin.register(FocusArea)
class FocusAreaAdmin(ImportExportModelAdmin):
    list_display = ["focus_area",
                    'id',
                    'updated',
                    'created']


# CategoryClients
@admin.register(CategoryClients)
class CategoryClientsAdmin(ImportExportModelAdmin):
    list_display = ["category_clients",
                    'id',
                    'updated',
                    'created']


# ContactTable
@admin.register(ContactTable)
class ContacttableAdmin(ImportExportModelAdmin):
    list_display = ['company_name',
                    'id',
                    'person_name',
                    'person_phone',
                    'person_email',
                    'contact_city',
                    'updated',
                    'created']


# admin.site.register(PaymentStatus)
@admin.register(PaymentStatus)
class PaymentStatusAdmin(ImportExportModelAdmin):
    list_display = ['status_name',
                    'id',
                    'updated',
                    'created']



# admin.site.register(BackendStaff)
@admin.register(BackendStaff)
class BackendStaffAdmin(ImportExportModelAdmin):
    list_display = ['backendstaff_name',
                    'id',
                    'updated',
                    'created']


# admin.site.register(Location)
@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    list_display = ['location_name',
                    'id',
                    'updated',
                    'created']


# admin.site.register(SubLocation)
@admin.register(SubLocation)
class SubLocationAdmin(ImportExportModelAdmin):
    list_display = ['country_name',
                    'id',
                    'updated',
                    'created']



# admin.site.register(Currency)
@admin.register(Currency)
class CurrencyAdmin(ImportExportModelAdmin):
    list_display = ['country_name',
                    'id',
                    'updated',
                    'created']


# admin.site.register(Gurantee)
@admin.register(Gurantee)
class GuranteeAdmin(ImportExportModelAdmin):
    list_display = ['gurantee',
                    'id',
                    'updated',
                    'created']




# admin.site.register(ArivalTable)
@admin.register(ArivalTable)
class ArivalTableAdmin(ImportExportModelAdmin):
    list_display = ['file_Ref',
                    'id',
                    'staff',
                    'agency_name',
                    'arival_date',
                    'inv_amount',
                    'updated',
                    'created']


# Feedbacks
@admin.register(Feedback)
class FeedbackAdmin(ImportExportModelAdmin):
    list_display = ('id', 'creator', 'suggestion_title',
                    'description',
                    'suport_file')
