from import_export import resources
from .models import *

# State
class StateResource(resources.ModelResource):
    class meta:
        model = State

# NewCompanyRegistration
class NewCompanyRegistrationResource(resources.ModelResource):
    class meta:
        model = NewCompanyRegistration

# CompanyKYCDetails
class CompanyKYCDetailsResource(resources.ModelResource):
    class meta:
        model = CompanyKYCDetails

# ContactTable
class ContactTableResource(resources.ModelResource):
    class meta:
        model = ContactTable

# FocusArea
class FocusAreaResource(resources.ModelResource):
    class meta:
        model = FocusArea

# CategoryClients
class CategoryClientsResource(resources.ModelResource):
    class meta:
        model = CategoryClients

# CompanyFullKYC
class CompanyFullKYCResource(resources.ModelResource):
    class meta:
        model = CompanyFullKYC

# Affiliations
class AffiliationsResource(resources.ModelResource):
    class meta:
        model = Affiliations

# OfficeRole
class OfficeRoleResource(resources.ModelResource):
    class meta:
        model = OfficeRole

# BackendStaff
class BackendStaffResource(resources.ModelResource):
    class meta:
        model = BackendStaff

# Location
class LocationResource(resources.ModelResource):
    class meta:
        model = Location

# SubLocation
class SubLocationResource(resources.ModelResource):
    class meta:
        model = SubLocation

# PaymentStatus
class PaymentStatusResource(resources.ModelResource):
    class meta:
        model = PaymentStatus

# ArivalTable
class ArivalTableResource(resources.ModelResource):
    class meta:
        model = ArivalTable

# Currency
class CurrencyResource(resources.ModelResource):
    class meta:
        model = Currency

# Gurantee
class GuranteeResource(resources.ModelResource):
    class meta:
        model = Gurantee

# StaffDetails
class StaffDetailsResource(resources.ModelResource):
    class meta:
        model = StaffDetails


# Feedback
class FeedbackResource(resources.ModelResource):
    class meta:
        model = Feedback