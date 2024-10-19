from django import forms
from django.forms import ModelForm
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactTable
        fields = '__all__'
        exclude = ['creator', 'editor',]
        widgets = {
            'company_name': forms.Select(attrs={"class": "form-control"}),
            'person_name': forms.TextInput(attrs={"class": "form-control"}),
            'person_phone': forms.TextInput(attrs={"class": "form-control"}),
            'person_email': forms.EmailInput(attrs={"class": "form-control"}),
            'contact_designation': forms.TextInput(attrs={"class": "form-control"}),
            'contact_local_area1': forms.TextInput(attrs={"class": "form-control"}),
            'contact_local_area2': forms.TextInput(attrs={"class": "form-control"}),
            'contact_city': forms.TextInput(attrs={"class": "form-control"}),
            'contact_state': forms.Select(attrs={"class": "form-control"}),
            'contact_pincode': forms.TextInput(attrs={"class": "form-control"}),
            'country': forms.TextInput(attrs={"class": "form-control"}),
            'dob': forms.DateInput(attrs={"class": "form-control" , 'type': 'date'}),
            'anniversary': forms.DateInput(attrs={"class": "form-control",  'type': 'date'}),
            'cat_client': forms.CheckboxSelectMultiple(attrs={"class": "form-check, form-check-inline", "type":"checkbox" }),
            'focus_area': forms.CheckboxSelectMultiple(attrs={"class": "form-check, form-check-inline","type":"checkbox"}),
            'contact_card': forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            'company_name': 'Company Name',  # Change the label for the 'company_name' field
            'person_name': 'Person Name',
            'contact_designation': 'Designation',
            'person_phone': 'Phone No',
            'person_email': 'Email ID',
            'contact_local_area1': 'Local Area 1',
            'contact_local_area2': 'Local Area 2',
            'contact_city': 'City',
            'contact_state': 'State',
            'contact_pincode': 'Pincode',
            'country': 'Country',
            'dob': 'DOB',
            'anniversary': 'Anniversary',
            'cat_client': 'Category of Client ',
            'focus_area': 'Focuse Area',
            'contact_card': 'Visiting Card',
        }

class ContactIndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualContactTable
        fields = '__all__'
        exclude = ['creator', 'editor',]
        widgets = {
            'company_name': forms.TextInput(attrs={"class": "form-control"}),
            'person_name': forms.TextInput(attrs={"class": "form-control"}),
            'person_phone': forms.TextInput(attrs={"class": "form-control"}),
            'person_email': forms.EmailInput(attrs={"class": "form-control"}),
            'contact_designation': forms.TextInput(attrs={"class": "form-control"}),
            'contact_local_area1': forms.TextInput(attrs={"class": "form-control"}),
            'contact_local_area2': forms.TextInput(attrs={"class": "form-control"}),
            'contact_city': forms.TextInput(attrs={"class": "form-control"}),
            'contact_state': forms.Select(attrs={"class": "form-control"}),
            'contact_pincode': forms.TextInput(attrs={"class": "form-control"}),
            'country': forms.TextInput(attrs={"class": "form-control"}),
            'dob': forms.DateInput(attrs={"class": "form-control" , 'type': 'date'}),
            'anniversary': forms.DateInput(attrs={"class": "form-control",  'type': 'date'}),
            'cat_client': forms.CheckboxSelectMultiple(attrs={"class": "form-check, form-check-inline", "type":"checkbox" }),
            'focus_area': forms.CheckboxSelectMultiple(attrs={"class": "form-check, form-check-inline","type":"checkbox"}),
            'contact_card': forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            'company_name': 'Company Name',  # Change the label for the 'company_name' field
            'person_name': 'Person Name',
            'contact_designation': 'Designation',
            'person_phone': 'Phone No',
            'person_email': 'Email ID',
            'contact_local_area1': 'Local Area 1',
            'contact_local_area2': 'Local Area 2',
            'contact_city': 'City',
            'contact_state': 'State',
            'contact_pincode': 'Pincode',
            'country': 'Country',
            'dob': 'DOB',
            'anniversary': 'Anniversary',
            'cat_client': 'Category of Client ',
            'focus_area': 'Focuse Area',
            'contact_card': 'Visiting Card',
        }


    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     if self.instance and self.instance.pk:
    #         # Form is being used to edit an existing instance
    #         self.fields['company_name'].disabled = True


class ArivalForm(forms.ModelForm):
    class Meta:
        model = ArivalTable
        fields = '__all__'
        exclude = ['creator', 'editor']
        widgets = {
            'sub_location': forms.Select(attrs={"class": "form-control"}),
            'location': forms.Select(attrs={"class": "form-control"}),
            'staff': forms.Select(attrs={"class": "form-control"}),
            'backend_staff': forms.Select(attrs={"class": "form-control"}),
            'confirmation_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'origin_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'arival_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'depart_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'file_Ref': forms.TextInput(attrs={"class": "form-control"}),
            'ground_partner_file_ref': forms.TextInput(attrs={"class": "form-control"}),
            'agency_name': forms.Select(attrs={"class": "form-control"}),
            'lead_pax_name': forms.TextInput(attrs={"class": "form-control"}),
            'lead_pax_number': forms.TextInput(attrs={"class": "form-control"}),
            'adt_pax': forms.TextInput(attrs={"class": "form-control"}),
            'child_pax': forms.TextInput(attrs={"class": "form-control"}),
            'adt_cost': forms.TextInput(attrs={"class": "form-control"}),
            'child_cost': forms.TextInput(attrs={"class": "form-control"}),
            'nights': forms.TextInput(attrs={"class": "form-control"}),
            'quality_check_by': forms.TextInput(attrs={"class": "form-control"}),
            'inv_num': forms.TextInput(attrs={"class": "form-control"}),
            'inv_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'currency': forms.Select(attrs={"class": "form-control"}),
            'currency_rate': forms.TextInput(attrs={"class": "form-control"}),
            'inv_amount': forms.TextInput(attrs={"class": "form-control"}),
            'payment_status': forms.Select(attrs={"class": "form-control"}),
            'folder_link': forms.TextInput(attrs={"class": "form-control"}),
            'amt_recev': forms.TextInput(attrs={"class": "form-control"}),
            # 'part_pmt_deadline': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            # 'final_pmt_amt': forms.TextInput(attrs={"class": "form-control"}),
            'final_pmt_deadline': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'payment_india': forms.TextInput(attrs={"class": "form-control"}),
            'itinerary_submit_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'purchase_amt': forms.TextInput(attrs={"class": "form-control"}),
            'markup_percentage': forms.TextInput(attrs={"class": "form-control"}),
            'visa_letter_submit_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'voucher_submit_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'agency_staff_name': forms.TextInput(attrs={"class": "form-control"}),
            'agency_staff_email': forms.EmailInput(attrs={"class": "form-control"}),
            'agency_staff_mobile': forms.TextInput(attrs={"class": "form-control"}),
            'package_details': forms.TextInput(attrs={"class": "form-control"}),
            'cdmc_remark': forms.TextInput(attrs={"class": "form-control"}),
            'ground_partner_remark': forms.TextInput(attrs={"class": "form-control"}),
            'sales_remark': forms.TextInput(attrs={"class": "form-control"}),
            'gurantee': forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'sub_location': 'Sub Location',
            'location': 'Location',
            'staff': 'Staff',
            'backend_staff': 'Backend Staff',
            'confirmation_date': 'Confirmation Date',
            'origin_date': 'Origin Date',
            'arival_date': 'Arival Date',
            'depart_date': 'Depart Date',
            'file_Ref': 'File Ref',
            'ground_partner_file_ref': 'Ground Partner File Ref',
            'agency_name': 'Agency Name',
            'lead_pax_name': 'Lead Pax Name',
            'lead_pax_number': 'Lead Pax Number',
            'adt_pax': 'Adt Pax',
            'child_pax': 'Child Pax',
            'adt_cost': 'Adt Cost',
            'child_cost': 'Child Cost',
            'nights': 'Nights',
            'quality_check_by': 'Quality Check By',
            'inv_num': 'Inv Num',
            'inv_date': 'Inv Date',
            'currency': 'Currency',
            'currency_rate' : 'Currency Rate',
            'inv_amount': 'Inv Amount',
            'payment_status': 'Payment Status',
            'folder_link': 'Folder Link',
            'amt_recev': 'Amt Received',
            # 'part_pmt_deadline': 'Part Pmt Deadline',
            # 'final_pmt_amt': 'Final Pmt Amt',
            'final_pmt_deadline': 'Final Pmt Deadline',
            'payment_india': 'Payment India',
            'itinerary_submit_date': 'Itinerary Submit Date',
            'purchase_amt': 'Purchase Amt',
            'markup_percentage': 'Markup Percentage',
            'visa_letter_submit_date': 'Visa Letter Submit Date',
            'voucher_submit_date': 'Voucher Submit Date',
            'agency_staff_name': 'Agency Staff Name',
            'agency_staff_email': 'Agency Staff Email',
            'agency_staff_mobile': 'Agency Staff Mobile',
            'package_details': 'Package Details',
            'cdmc_remark': 'Cdmc Remark',
            'ground_partner_remark': 'Ground Partner Remark',
            'sales_remark': 'Sales Remark',
            'gurantee': 'Gurantee',
        }

        help_texts = {
            'currency_rate': 'Please enter currency rate related to USD like :- If your invoice amount is in INR and 500, and currency rate is 1 USD = 84.07 INR, You enter 84.07 only, so that in USD amount will be 5.95 USD ',
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')
    start_date = forms.DateField(
        required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(
        required=False, widget=forms.TextInput(attrs={'type': 'date'}))


class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model = StaffDetails
        fields = '__all__'
        exclude = ['username']
        widgets = {
            'user_full_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'job': forms.TextInput(attrs={"class": "form-control"}),
            'bio': forms.Textarea(attrs={"class": "form-control"}),
            'address': forms.Textarea(attrs={"class": "form-control"}),
            'city': forms.TextInput(attrs={"class": "form-control"}),
            'state': forms.Select(attrs={"class": "form-control"}),
            'pincode': forms.TextInput(attrs={"class": "form-control"}),
            'avatar': forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            'user_full_name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone',
            'job': 'Designation',
            'bio': 'About',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'pincode': 'Pincode',
            'avatar': 'Profile Picture'}


class NewCompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = NewCompanyRegistration
        fields = '__all__'
        exclude = ['creator', 'updater', 'kyc_status']
        widgets = {
            'company_name': forms.TextInput(attrs={"class": "form-control"}),
            'gst_number': forms.TextInput(attrs={"class": "form-control"}),
            'company_address': forms.Textarea(attrs={"class": "form-control"}),
            'company_city': forms.TextInput(attrs={"class": "form-control"}),
            'company_state': forms.Select(attrs={"class": "form-control"}),
            'company_pincode': forms.TextInput(attrs={"class": "form-control"}),
            'person_name': forms.TextInput(attrs={"class": "form-control"}),
            'person_phone': forms.TextInput(attrs={"class": "form-control"}),
            'person_email': forms.EmailInput(attrs={"class": "form-control"}),
            'person_designation': forms.TextInput(attrs={"class": "form-control"})
        }
        labels = {
            'company_name': ' New Company Name',
            'gst_number': 'GSTIN :',
            'company_address': 'Company Address ',
            'company_city': ' Company City',
            'company_state': ' State',
            'company_pincode': 'Pincode',
            'person_name': 'Contact Person Name',
            'person_phone': 'Phone',
            'person_email': 'Email',
            'person_designation': 'Designation'}
        
    def __init__(self, *args, **kwargs):
        super(NewCompanyRegistrationForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Form is being used to edit an existing instance
            self.fields['company_name'].disabled = True


class CompanyKYCForm(ModelForm):
    class Meta:
        model = CompanyKYCDetails
        fields = '__all__'
        exclude = ['creator', 'editor']
        widgets = {
            'company_kyc': forms.Select(attrs={"class": "form-control"}),
            'company_branch': forms.TextInput(attrs={"class": "form-control"}),
            'Constitution': forms.TextInput(attrs={"class": "form-control"}),
            'office_role': forms.Select(attrs={"class": "form-control"}),
            'pancard_no': forms.TextInput(attrs={"class": "form-control"}),
            'pancard_file': forms.FileInput(attrs={"class": "form-control"}),
            'gstin': forms.TextInput(attrs={"class": "form-control"}),
            'gstin_file': forms.FileInput(attrs={"class": "form-control"}),
            'msme_no': forms.TextInput(attrs={"class": "form-control"}),
            'msme_file': forms.FileInput(attrs={"class": "form-control"}),
            'company_reg_address': forms.Textarea(attrs={"class": "form-control"}),
            'company_city': forms.TextInput(attrs={"class": "form-control"}),
            'company_state': forms.Select(attrs={"class": "form-control"}),
            'company_pincode': forms.TextInput(attrs={"class": "form-control"}),
            'company_email': forms.EmailInput(attrs={"class": "form-control"}),
            'company_landline': forms.TextInput(attrs={"class": "form-control"}),
            'company_Affiliations': forms.Select(attrs={"class": "form-control"}),
            'introduced_by': forms.TextInput(attrs={"class": "form-control"}),
            'team_size': forms.TextInput(attrs={"class": "form-control"}),
            'relationship_manager': forms.TextInput(attrs={"class": "form-control"}),
            'rating': forms.TextInput(attrs={"class": "form-control"}),
            'productivity_previous': forms.TextInput(attrs={"class": "form-control"}),
            'productivity_second_previous': forms.TextInput(attrs={"class": "form-control"}),
            'cat_client': forms.CheckboxSelectMultiple(attrs={"class": "form-check, form-check-inline", "type":"checkbox" }),
            'focus_area': forms.CheckboxSelectMultiple(attrs={"class": "form-check, form-check-inline","type":"checkbox"}),
        }
        labels = {
            'company_kyc': ' Company Name',
            'company_branch': 'Company Branch',
            'Constitution': 'Constitution',
            'office_role': 'Office Role',
            'pancard_no': 'Pan Card',
            'pancard_file': 'Pan File',
            'gstin': 'GSTIN',
            'gstin_file': 'GSTIN File',
            'msme_no': 'MSME',
            'msme_file': 'MSME File',
            'company_reg_address': 'Company Registered Address',
            'company_city': 'City',
            'company_state': 'State',
            'company_pincode': 'Pincode',
            'company_email': 'Email ID',
            'company_landline': 'Landline',
            'company_Affiliations': 'Affiliations',
            'introduced_by': 'Introduced By',
            'team_size': 'Team Size',
            'relationship_manager': 'Relationship Manager',
            'rating': 'Rating',
            'productivity_previous': 'Productivity Last FY',
            'productivity_second_previous': 'Productivity Second Last FY',
            'cat_client': 'Category of Clients',
            'focus_area': 'Focus Area' }

    def __init__(self, *args, **kwargs):
        super(CompanyKYCForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Form is being used to edit an existing instance
            self.fields['company_kyc'].disabled = True


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ['creator', 'editor', 'status']
        widgets = {
            'suggestion_title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'suport_file': forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            'suggestion_title': 'Any Suggestion',
            'description': 'Explain In Details ',
            'suport_file': 'Attach File',

        }
