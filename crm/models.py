from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class State(models.Model):
    state_name = models.CharField(max_length=255)
    state_code = models.CharField(max_length=2)
    gstin_code = models.CharField(max_length=2)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.state_name


class StaffDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_full_name = models.CharField(max_length=150, default='Test')
    job= models.CharField(max_length=255, blank=True , default='staff')
    email = models.CharField(max_length=200, blank=True, default="a@gmail.com")
    phone = models.CharField(max_length=10, blank=True, default=123)
    bio = models.TextField(null=True) 
    address = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    pincode = models.CharField(max_length=6, blank=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg")

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.user_full_name

class CompanyFullKYC(models.Model):
    company_name = models.CharField(max_length=200)
    kyc_status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.company_name

# Currently this Table is not in use
class NewCompanyRegistration(models.Model):
    creator = models.ForeignKey(User, related_name='newcreator',on_delete=models.SET_NULL, null=True, blank=True)
    updater = models.ForeignKey(User, related_name="updater", on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    gst_number = models.CharField(max_length=16, blank=True, null=True)
    company_address = models.CharField(max_length=200)
    company_city = models.CharField(max_length=100, blank=True)
    company_state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    company_pincode = models.CharField(max_length=6, blank=True)
    person_name = models.CharField(max_length=200)
    person_phone = models.CharField(max_length=10)
    person_email = models.EmailField(max_length=100)
    person_designation = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.company_name

    
class OfficeRole(models.Model):
    office_role = models.CharField(max_length=255)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.office_role
    
class Affiliations(models.Model):
    affiliations = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.affiliations
    
class CompanyKYCDetails(models.Model):
    creator = models.ForeignKey(User, related_name='creator',on_delete=models.SET_NULL, null=True, blank=True)
    editor = models.ForeignKey(User, related_name="editor", on_delete=models.SET_NULL, null=True, blank=True)
    company_kyc = models.ForeignKey(CompanyFullKYC, on_delete=models.SET_NULL, null=True)
    company_branch = models.CharField(max_length=150)    
    Constitution = models.CharField(max_length=255)
    office_role = models.ForeignKey(OfficeRole, on_delete=models.SET_NULL, null=True)
    pancard_no = models.CharField(max_length=255)
    pancard_file = models.ImageField(null=True, default="file.png")
    gstin = models.CharField(max_length=255)
    gstin_file = models.ImageField(null=True, default="file.png")
    msme_no = models.CharField(max_length=255)
    msme_file = models.ImageField(null=True, default="file.png")
    company_reg_address = models.CharField(max_length=255)
    company_city = models.CharField(max_length=255)
    company_state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    company_pincode = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_landline = models.CharField(max_length=255)
    company_Affiliations = models.ForeignKey(Affiliations, on_delete=models.SET_NULL, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.company_kyc.company_name
    
class FocusArea(models.Model):
    focus_area = models.CharField(max_length=200)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.focus_area

class CategoryClients(models.Model):
    category_clients = models.CharField(max_length=200)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.category_clients



class ContactTable(models.Model):
    creator = models.ForeignKey(User, related_name='contactcreator',on_delete=models.SET_NULL, null=True, blank=True)
    editor = models.ForeignKey(User, related_name="contacteditor", on_delete=models.SET_NULL, null=True, blank=True)
    company_name = models.ForeignKey(
        CompanyFullKYC, on_delete=models.CASCADE, null=True, blank=True)
    person_name = models.CharField(max_length=200)
    contact_designation = models.CharField(max_length=255)
    person_phone = models.CharField(max_length=10)
    person_email = models.EmailField(max_length=100)
    contact_local_area1 = models.CharField(max_length=255, blank=True)
    contact_local_area2 = models.CharField(max_length=255, blank=True )
    contact_city = models.CharField(max_length=255, blank=True)
    contact_state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    contact_pincode = models.CharField(max_length=255, blank=True)
    cat_client = models.ForeignKey(CategoryClients, on_delete=models.SET_NULL,null=True,blank=True)
    focus_area = models.ForeignKey(FocusArea, on_delete=models.SET_NULL,null=True,blank=True)
    contact_card = models.ImageField(null=True,  default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.person_name


class PaymentStatus(models.Model):
    status_name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.status_name


# class Staff(models.Model):
#     staff_name = models.CharField(max_length=100)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return self.staff_name


class BackendStaff(models.Model):
    backendstaff_name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.backendstaff_name


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.location_name


class SubLocation(models.Model):
    country_name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.country_name


class Currency(models.Model):
    country_name = models.ForeignKey(
        SubLocation, on_delete=models.DO_NOTHING, null=True)
    country_code = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.currency


class Gurantee(models.Model):
    gurantee = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.gurantee


class ArivalTable(models.Model):
    creator = models.ForeignKey(User, related_name='arivalcreator',on_delete=models.SET_NULL, null=True, blank=True)
    editor = models.ForeignKey(User, related_name="arivaleditor", on_delete=models.SET_NULL, null=True, blank=True)
    sub_location = models.ForeignKey(
        SubLocation, on_delete=models.DO_NOTHING, null=True)
    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, null=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.DO_NOTHING, null=True)
    backend_staff = models.ForeignKey(
        BackendStaff, on_delete=models.DO_NOTHING, null=True)
    confirmation_date = models.DateField()
    origin_date = models.DateField()
    arival_date = models.DateField()
    depart_date = models.DateField()
    file_Ref = models.CharField(max_length=100, blank=True, null=True)
    ground_partner_file_ref = models.CharField(
        max_length=100, blank=True, null=True)
    agency_name = models.ForeignKey(
        CompanyKYCDetails, on_delete=models.DO_NOTHING, null=True)
    lead_pax_name = models.CharField(max_length=100, blank=True, null=True)
    lead_pax_number = models.CharField(max_length=100, blank=True, null=True)
    adt_pax = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    child_pax = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    adt_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    child_cost = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    nights = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    quality_check_by = models.CharField(max_length=100, blank=True, null=True)
    inv_num = models.CharField(max_length=100, blank=True, null=True)
    inv_date = models.DateField(null=True, blank=True)
    currency = models.ForeignKey(
        Currency, on_delete=models.DO_NOTHING, null=True)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    inv_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    payment_status = models.ForeignKey(
        PaymentStatus, models.DO_NOTHING, blank=True, null=True)
    folder_link = models.CharField(max_length=100, blank=True, null=True)
    amt_recev = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # part_pmt_amt = amt_recev
    # part_pmt_deadline = models.DateField(blank=True,null=True)
    # final_pmt_amt = models.CharField(max_length=100, blank=True, null=True)
    final_pmt_deadline = models.DateField(blank=True,null=True)
    payment_india = models.CharField(max_length=100, blank=True, null=True)
    itinerary_submit_date = models.DateField(blank=True,null=True)
    purchase_amt = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    markup_percentage = models.CharField(max_length=100, blank=True, null=True)
    visa_letter_submit_date = models.DateField(blank=True,null=True)
    voucher_submit_date = models.DateField(blank=True,null=True)
    agency_staff_name = models.CharField(max_length=100, blank=True, null=True)
    agency_staff_email = models.CharField(
        max_length=100, blank=True, null=True)
    agency_staff_mobile = models.CharField(
        max_length=100, blank=True, null=True)
    package_details = models.CharField(max_length=100, blank=True, null=True)
    cdmc_remark = models.CharField(max_length=100, blank=True, null=True)
    ground_partner_remark = models.CharField(
        max_length=100, blank=True, null=True)
    sales_remark = models.CharField(max_length=100, blank=True, null=True)
    gurantee = models.ForeignKey(
        Gurantee, on_delete=models.DO_NOTHING, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.file_Ref


class Feedback(models.Model):
    creator = models.ForeignKey(User, related_name='feedbackcreator',on_delete=models.SET_NULL, null=True, blank=True)
    editor = models.ForeignKey(User, related_name="feedbackeditor", on_delete=models.SET_NULL, null=True, blank=True)
    suggestion_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    suport_file = models.ImageField(blank=True, default="file.png")
    status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)