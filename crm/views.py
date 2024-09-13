from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.db.models import Q
import json
from django.http import JsonResponse
import os
from datetime import datetime
from django.db.models import Sum, F

# Create your views here.


@login_required(login_url='loginpage')
def home(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    all_arrival_data = ArivalTable.objects.all()
    # all_arrivals = ArivalTable.objects.count()

    # all_companies = CompanyFullKYC.objects.count()
    # kyc_companies = CompanyFullKYC.objects.filter(kyc_status=True).count()

    total_sale = ArivalTable.objects.aggregate(
        total=Sum(F('inv_amount') * F('currency_rate'))
    )['total']

    total_pur = ArivalTable.objects.aggregate(
        total=Sum(F('purchase_amt') * F('currency_rate'))
    )['total']

    gps = int(total_sale) - int(total_pur)
    # print(gp)
    if request.user.is_staff:
        all_arrivals = ArivalTable.objects.count()
        all_companies = CompanyFullKYC.objects.count()
        kyc_companies = CompanyFullKYC.objects.filter(kyc_status=True).count()

        sales_Agency = ArivalTable.objects.values('agency_name__company_kyc__company_name').annotate(
            total_inv_amount=Sum('inv_amount')).order_by('-total_inv_amount')[:5]

        sales_Location = ArivalTable.objects.values('sub_location__country_name').annotate(
            total_inv_amount=Sum('inv_amount')).order_by('-total_inv_amount')[:5]

        total_sale = ArivalTable.objects.aggregate(
            total=Sum(F('inv_amount') * F('currency_rate'))
        )['total']

        total_pur = ArivalTable.objects.aggregate(
            total=Sum(F('purchase_amt') * F('currency_rate'))
        )['total']

        gps = int(total_sale) - int(total_pur)

    else:
        all_arrivals = ArivalTable.objects.filter(creator=request.user).count()
        all_companies = ContactTable.objects.filter(
            creator=request.user).values('company_name').distinct().count()
        kyc_companies = 0

        sales_Agency = ArivalTable.objects.filter(creator=request.user).values('agency_name__company_kyc__company_name').annotate(
            total_inv_amount=Sum('inv_amount')).order_by('-total_inv_amount')[:5]

        sales_Location = ArivalTable.objects.filter(creator=request.user).values('sub_location__country_name').annotate(
            total_inv_amount=Sum('inv_amount')).order_by('-total_inv_amount')[:5]

        total_sale = ArivalTable.objects.filter(creator=request.user).aggregate(
            total=Sum(F('inv_amount') * F('currency_rate'))
        )['total']

        total_pur = ArivalTable.objects.filter(creator=request.user).aggregate(
            total=Sum(F('purchase_amt') * F('currency_rate'))
        )['total']

        gps = int(total_sale) - int(total_pur)

    # if condition end

    agency_data = [{'name': entry['agency_name__company_kyc__company_name'], 'value': float(
        entry['total_inv_amount'])} for entry in sales_Agency]

    location_data = [{'name': entry['sub_location__country_name'], 'value': float(
        entry['total_inv_amount'])} for entry in sales_Location]
    # print(data)
    agency_names = [item['name'] for item in agency_data]
    agency_values = [item['value'] for item in agency_data]

    # print("hello")
    # Aggregate data by salesperson
    sales_data = ArivalTable.objects.values('staff__user_full_name').annotate(
        total_inv_amount=Sum('inv_amount')).order_by('staff__user_full_name')
    # print("sales_data")
    # Format the data into the desired structure
    data = [{'name': entry['staff__user_full_name'], 'value': float(
        entry['total_inv_amount'])} for entry in sales_data]
    # print(data)
    names = [item['name'] for item in data]
    values = [item['value'] for item in data]

    pur_data = ArivalTable.objects.values('staff__user_full_name').annotate(
        total_inv_amount=Sum('purchase_amt')).order_by('staff__user_full_name')

    data2 = [{'name': entry['staff__user_full_name'],
              'value': float(entry['total_inv_amount'])} for entry in pur_data]
    # print(data)
    value = [item['value'] for item in data2]

    # Create dictionaries for easy lookup
    data_dict = {item['name']: item['value'] for item in data}
    data2_dict = {item['name']: item['value'] for item in data2}

    # Calculate the difference
    gp_data = []
    for name in data_dict:
        value1 = data_dict.get(name, 0)
        value2 = data2_dict.get(name, 0)
        difference = value1 - value2
        gp_data.append({'name': name, 'value': difference})

    gp = [item['value'] for item in gp_data]
    # print(gp_data)

    context = {
        'staff_data': statf_data,
        'all_arrivals': all_arrivals,
        'total_sum': total_sale,
        'all_companies': all_companies,
        'kyc_companies': kyc_companies,
        'total_pur': total_pur,
        'gps': gps,
        'data': data,
        'names': names,
        'values': values,
        'value': value,
        'gp': gp,
        'gp_data': gp_data,
        'all_arrival_data': all_arrival_data,
        'agency_names': agency_names,
        'agency_values': agency_values,
        'agency_data': agency_data,
        'location_data': location_data,
    }

    return render(request, 'dashboard/dashboard_home.html', context)


@login_required(login_url='loginpage')
def profilepage(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    context = {'staff_data': statf_data}
    return render(request, 'crm_profile/user_overview.html', context)


@login_required(login_url='loginpage')
def profileedit(request, pk):
    statf_data = StaffDetails.objects.get(id=pk)
    if request.method == "POST":
        # Process the form submission with the existing company instance
        form = StaffDetailsForm(
            request.POST, request.FILES, instance=statf_data)
        if form.is_valid():
            user_details = form.save(commit=False)
            if request.FILES.get('avatar'):
                profile_file = request.FILES['avatar']
                ext_profile = profile_file.name.split(
                    '.')[-1]  # Get file extension
                new_profile = f"{form.cleaned_data['user_full_name']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_profile}"
                user_details.avatar.name = os.path.join('photos/', new_profile)

            form.save()  # Save the updated instance

            return redirect('profilepage')
    else:
        form = StaffDetailsForm(instance=statf_data)

    context = {'staff_data': statf_data,
               'form': form}
    return render(request, 'crm_profile/user_edit.html', context)

# New Company Registration Codes

# This function is not in work


@login_required(login_url='loginpage')
def newcompanyregistration(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    form = NewCompanyRegistrationForm()
    companies = CompanyFullKYC.objects.all()
    if request.method == 'POST':
        comp_reg = request.POST.get('company_name')
        company, created = CompanyFullKYC.objects.get_or_create(
            company_name=comp_reg)
        form = NewCompanyRegistrationForm(request.POST)
        if form.is_valid():
            comp_regs = form.save(commit=False)
            comp_regs.creator = request.user
            comp_regs.company_name = company
            form.save()
            return redirect('newcomp')
    context = {
        'companies': companies,
        'form': form,
        'staff_data': statf_data,

    }
    return render(request, 'new_company_registration/new_comp_reg.html', context)

# This function is not in work


@login_required(login_url='loginpage')
def newcompanyedit(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    company_data = NewCompanyRegistration.objects.get(id=pk)
    if request.method == "POST":
        # Process the form submission with the existing company instance
        form = NewCompanyRegistrationForm(request.POST, instance=company_data)
        if form.is_valid():
            comp_regs = form.save(commit=False)
            comp_regs.updater = request.user
            form.save()  # Save the updated instance
            return redirect('newcomp')
    else:
        form = NewCompanyRegistrationForm(instance=company_data)

    context = {
        'form': form,
        'staff_data': statf_data,
        'company_data': company_data
    }
    return render(request, 'new_company_registration/new_comp_edit.html', context)


@login_required(login_url='loginpage')
def allnewcompany(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    # queryset = NewCompanyRegistration.objects.all()
    queryset = CompanyFullKYC.objects.all()
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')
        if query:
            queryset = queryset.filter(
                Q(person_name__icontains=query) |
                Q(person_email__icontains=query) |
                Q(person_phone__icontains=query) |
                Q(company_name__company_name__icontains=query)
            )
        if start_date and end_date:
            queryset = queryset.filter(
                updated__date__range=(start_date, end_date)
            )

    paginator = Paginator(queryset, 15)  # Show 8 items per page
    page_number = request.GET.get('page')
    company_data = paginator.get_page(page_number)
    context = {
        'company_data': company_data,
        'staff_data': statf_data,
        'search_form': search_form,
    }
    return render(request, 'new_company_registration/all_new_comp.html', context)

# This function is not in work


@login_required(login_url='loginpage')
def companyoverview(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    company_data = NewCompanyRegistration.objects.get(id=pk)
    context = {
        'company_data': company_data,
        'staff_data': statf_data
    }
    return render(request, 'new_company_registration/new_comp_overview.html', context)


@login_required(login_url='loginpage')
def newcompanydelete(request, pk):
    company = NewCompanyRegistration.objects.get(id=pk)
    company.delete()
    return redirect('newcomp')


#  Full KYC Company Section
@login_required(login_url='loginpage')
def addcompanykyc(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    form = CompanyKYCForm()
    # companies = CompanyFullKYC.objects.all()
    if request.method == 'POST':
        company_kyc = request.POST.get('company_kyc')
        kyc_val = CompanyFullKYC.objects.get(id=company_kyc)
        print(kyc_val.kyc_status)
        if kyc_val.kyc_status == False:  # Check that what value is set there if false the set true neither do nothing
            kyc_val.kyc_status = True  # now set value True
            kyc_val.save()  # save the instance
        print(kyc_val.kyc_status)
        form = CompanyKYCForm(request.POST, request.FILES)
        if form.is_valid():
            comp_kyc_data = form.save(commit=False)

            if request.FILES.get('gstin_file'):
                gst_file = request.FILES['gstin_file']
                ext_gst = gst_file.name.split('.')[-1]  # Get file extension
                new_gst = f"{form.cleaned_data['company_kyc']}_gst_{form.cleaned_data['gstin']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_gst}"
                comp_kyc_data.gstin_file.name = os.path.join('gstin/', new_gst)

            if request.FILES.get('pancard_file'):
                pan_file = request.FILES['pancard_file']
                ext_pan = pan_file.name.split('.')[-1]  # Get file extension
                new_pan = f"{form.cleaned_data['company_kyc']}_pan_{form.cleaned_data['pancard_no']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_pan}"
                comp_kyc_data.pancard_file.name = os.path.join('pan/', new_pan)

            if request.FILES.get('msme_file'):
                msme_file = request.FILES['msme_file']
                ext_msme = msme_file.name.split('.')[-1]  # Get file extension
                new_msme = f"{form.cleaned_data['company_kyc']}_msme_{form.cleaned_data['msme_no']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_msme}"
                comp_kyc_data.msme_file.name = os.path.join('msme/', new_msme)

            comp_kyc_data.creator = request.user
            form.save()
            return redirect('allcompanykyc')

    context = {
        'form': form,
        'staff_data': statf_data,
    }
    return render(request, 'company_kyc/comp_kyc_add.html', context)


@login_required(login_url='loginpage')
def editcompanykyc(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    company_data = CompanyKYCDetails.objects.get(id=pk)
    if request.method == "POST":
        # Process the form submission with the existing company instance
        form = CompanyKYCForm(request.POST, request.FILES,
                              instance=company_data)
        if form.is_valid():
            comp_kyc_edit = form.save(commit=False)
            comp_kyc_edit.editor = request.user

            if request.FILES.get('gstin_file'):
                gst_file = request.FILES['gstin_file']
                ext_gst = gst_file.name.split('.')[-1]  # Get file extension
                new_gst = f"{form.cleaned_data['company_kyc']}_gst_{form.cleaned_data['gstin']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_gst}"
                comp_kyc_edit.gstin_file.name = os.path.join('gstin/', new_gst)

            if request.FILES.get('pancard_file'):
                pan_file = request.FILES['pancard_file']
                ext_pan = pan_file.name.split('.')[-1]  # Get file extension
                new_pan = f"{form.cleaned_data['company_kyc']}_pan_{form.cleaned_data['pancard_no']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_pan}"
                comp_kyc_edit.pancard_file.name = os.path.join('pan/', new_pan)

            if request.FILES.get('msme_file'):
                msme_file = request.FILES['msme_file']
                ext_msme = msme_file.name.split('.')[-1]  # Get file extension
                new_msme = f"{form.cleaned_data['company_kyc']}_msme_{form.cleaned_data['msme_no']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_msme}"
                comp_kyc_edit.msme_file.name = os.path.join('msme/', new_msme)

            # comp_kyc_edit.company_kyc = company_data.company_name
            form.save()  # Save the updated instance
            return redirect('allcompanykyc')
        # else:
        #     print('someyhing error', form.errors)
    else:
        form = CompanyKYCForm(instance=company_data)

    context = {
        'form': form,
        'staff_data': statf_data,
        'company_data': company_data
    }
    return render(request, 'company_kyc/comp_edit.html', context)


@login_required(login_url='loginpage')
def allcompanykyc(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    queryset = CompanyKYCDetails.objects.all()
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')
        if query:
            queryset = queryset.filter(
                Q(company_branch__icontains=query) |
                Q(Constitution__icontains=query) |
                Q(gstin__icontains=query) |
                Q(company_kyc__company_name__icontains=query)
            )
        if start_date and end_date:
            queryset = queryset.filter(
                updated__date__range=(start_date, end_date)
            )

    paginator = Paginator(queryset, 15)  # Show 8 items per page
    page_number = request.GET.get('page')
    company_data = paginator.get_page(page_number)
    context = {
        'company_data': company_data,
        'staff_data': statf_data,
        'search_form': search_form,
    }
    return render(request, 'company_kyc/comp_kyc_table.html', context)


@login_required(login_url='loginpage')
def overviewcompanykyc(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    company_data = CompanyKYCDetails.objects.get(id=pk)
    context = {
        'company_data': company_data,
        'staff_data': statf_data
    }
    return render(request, 'company_kyc/comp_overview.html', context)


@login_required(login_url='loginpage')
def deletecompanykyc(request, pk):
    company = CompanyKYCDetails.objects.get(id=pk)
    company_full = company.company_kyc
    # print(company_full.kyc_status)
    company_full.kyc_status = False
    company_full.save()
    # print(company_full.kyc_status)
    company.delete()
    return redirect('newcomp')

# End Company KYC Functions

#  Company Contacts Section


@login_required(login_url='loginpage')
def addcontact(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    form = ContactForm()
    companies = CompanyFullKYC.objects.all()
    if request.method == 'POST':
        comp_reg = request.POST.get('company_name')
        company, created = CompanyFullKYC.objects.get_or_create(
            company_name=comp_reg)
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            comp_kyc_data = form.save(commit=False)

            if request.FILES.get('contact_card'):
                visiting_file = request.FILES['contact_card']
                ext_visiting = visiting_file.name.split(
                    '.')[-1]  # Get file extension
                new_visiting = f"{form.cleaned_data['person_name']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_visiting}"
                comp_kyc_data.contact_card.name = os.path.join(
                    'visitingcard/', new_visiting)

            comp_kyc_data.creator = request.user
            comp_kyc_data.company_name = company
            form.save()
            return redirect('allcontact')
    context = {
        'form': form,
        'staff_data': statf_data,
        'companies': companies,
    }
    return render(request, 'contacts/contact_add.html', context)


@login_required(login_url='loginpage')
def editcontact(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    contact_data = ContactTable.objects.get(id=pk)
    companies = CompanyFullKYC.objects.all()
    if request.method == "POST":
        # comp_reg = request.POST.get('company_name')
        # company, created = CompanyFullKYC.objects.get_or_create(
        #     company_name=comp_reg)
        # Process the form submission with the existing company instance
        form = ContactForm(request.POST, request.FILES, instance=contact_data)
        if form.is_valid():
            comp_kyc_edit = form.save(commit=False)

            if request.FILES.get('contact_card'):
                visiting_file = request.FILES['contact_card']
                ext_visiting = visiting_file.name.split(
                    '.')[-1]  # Get file extension
                new_visiting = f"{form.cleaned_data['person_name']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_visiting}"
                comp_kyc_edit.contact_card.name = os.path.join(
                    'visitingcard/', new_visiting)

            comp_kyc_edit.editor = request.user
            # comp_kyc_edit.company_name = company
            form.save()  # Save the updated instance
            return redirect('allcontact')
        # else:
        #     print('someyhing error', form.errors)
    else:
        form = ContactForm(instance=contact_data)

    context = {
        'form': form,
        'staff_data': statf_data,
        'contact_data': contact_data,
        'companies': companies,
    }
    return render(request, 'contacts/contact_edit.html', context)


@login_required(login_url='loginpage')
def allcontact(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    queryset = ContactTable.objects.all()
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')
        if query:
            queryset = queryset.filter(
                Q(person_name__icontains=query) |
                Q(person_phone__icontains=query) |
                Q(contact_city__icontains=query) |
                Q(person_email__icontains=query) |
                Q(company_name__company_name__icontains=query)
            )
        if start_date and end_date:
            queryset = queryset.filter(
                updated__date__range=(start_date, end_date)
            )

    paginator = Paginator(queryset, 15)  # Show 8 items per page
    page_number = request.GET.get('page')
    contact_data = paginator.get_page(page_number)
    context = {
        'contact_data': contact_data,
        'staff_data': statf_data,
        'search_form': search_form
    }
    return render(request, 'contacts/contact_table.html', context)


@login_required(login_url='loginpage')
def overviewcontact(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    contact_data = ContactTable.objects.get(id=pk)
    context = {
        'contact_data': contact_data,
        'staff_data': statf_data
    }
    return render(request, 'contacts/contact_overview.html', context)


@login_required(login_url='loginpage')
def deletecontact(request, pk):
    contact = ContactTable.objects.get(id=pk)
    contact.delete()
    return redirect('allcontact')

# End Contact Details Functions


#  Arrivals Section
@login_required(login_url='loginpage')
def addarrival(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    form = ArivalForm()
    # companies = CompanyFullKYC.objects.all()
    if request.method == 'POST':
        form = ArivalForm(request.POST, request.FILES)
        if form.is_valid():
            arrival_data = form.save(commit=False)
            arrival_data.creator = request.user
            form.save()
            return redirect('allarrival')

    context = {
        'form': form,
        'staff_data': statf_data,
    }
    return render(request, 'arrivals/arrival_add.html', context)


@login_required(login_url='loginpage')
def editarrival(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    arrival_data = ArivalTable.objects.get(id=pk)
    if request.method == "POST":
        # Process the form submission with the existing company instance
        form = ArivalForm(request.POST, request.FILES, instance=arrival_data)
        if form.is_valid():
            arrival_edit = form.save(commit=False)
            arrival_edit.editor = request.user
            form.save()  # Save the updated instance
            return redirect('allarrival')
        # else:
        #     print('someyhing error', form.errors)
    else:
        form = ArivalForm(instance=arrival_data)

    context = {
        'form': form,
        'staff_data': statf_data,
        'arrival_data': arrival_data
    }
    return render(request, 'arrivals/arrival_edit.html', context)


@login_required(login_url='loginpage')
def allarrival(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    # arrival_data =
    queryset = ArivalTable.objects.all()
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')
        if query:
            queryset = queryset.filter(
                Q(staff__username__username__icontains=query) |
                Q(file_Ref__icontains=query) |
                Q(lead_pax_name__icontains=query) |
                Q(agency_name__company_name__icontains=query)
            )
        if start_date and end_date:
            queryset = queryset.filter(
                updated__date__range=(start_date, end_date)
            )

    paginator = Paginator(queryset, 15)  # Show 8 items per page
    page_number = request.GET.get('page')
    arrival_data = paginator.get_page(page_number)
    context = {
        'arrival_data': arrival_data,
        'staff_data': statf_data,
        'search_form': search_form,
    }
    return render(request, 'arrivals/arrival_table.html', context)


@login_required(login_url='loginpage')
def overviewarrival(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    arrival_data = ArivalTable.objects.get(id=pk)
    context = {
        'arrival_data': arrival_data,
        'staff_data': statf_data
    }
    return render(request, 'arrivals/arrival_overview.html', context)


@login_required(login_url='loginpage')
def deletearrival(request, pk):
    arrival = ArivalTable.objects.get(id=pk)
    arrival.delete()
    return redirect('allarrival')

# End Arrivals Details Functions


#  Any Feedbacks Section


@login_required(login_url='loginpage')
def addfeedback(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            comp_kyc_data = form.save(commit=False)

            if request.FILES.get('suport_file'):
                feedback_file = request.FILES['suport_file']
                ext_feedback = feedback_file.name.split(
                    '.')[-1]  # Get file extension
                new_feedback = f"{form.cleaned_data['suggestion_title']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_feedback}"
                comp_kyc_data.suport_file.name = os.path.join(
                    'feedback/', new_feedback)

            comp_kyc_data.creator = request.user
            form.save()
            return redirect('allfeedback')

    context = {
        'form': form,
        'staff_data': statf_data,
    }
    return render(request, 'feedback/feedback_add.html', context)


@login_required(login_url='loginpage')
def editfeedback(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    feedback_data = Feedback.objects.get(id=pk)
    if request.method == "POST":
        # Process the form submission with the existing company instance
        form = FeedbackForm(request.POST, request.FILES,
                            instance=feedback_data)
        if form.is_valid():
            comp_kyc_edit = form.save(commit=False)

            if request.FILES.get('suport_file'):
                feedback_file = request.FILES['suport_file']
                ext_feedback = feedback_file.name.split(
                    '.')[-1]  # Get file extension
                new_feedback = f"{form.cleaned_data['suggestion_title']}_{
                    datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_feedback}"
                comp_kyc_edit.suport_file.name = os.path.join(
                    'feedback/', new_feedback)

            comp_kyc_edit.editor = request.user
            form.save()  # Save the updated instance
            return redirect('allfeedback')
            messages.success(request, "updated successfully")
    else:
        form = FeedbackForm(instance=feedback_data)
        messages.error(request, "Something error")

    context = {
        'form': form,
        'staff_data': statf_data,
        'feedback_data': feedback_data
    }
    return render(request, 'feedback/feedback_edit.html', context)


@login_required(login_url='loginpage')
def allfeedback(request):
    statf_data = StaffDetails.objects.get(username=request.user)
    queryset = Feedback.objects.all()
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        start_date = search_form.cleaned_data.get('start_date')
        end_date = search_form.cleaned_data.get('end_date')
        if query:
            queryset = queryset.filter(
                Q(creator__username__icontains=query) |
                Q(suggestion_title__icontains=query) |
                Q(description__icontains=query)
            )
        if start_date and end_date:
            queryset = queryset.filter(
                updated__date__range=(start_date, end_date)
            )

    paginator = Paginator(queryset, 15)  # Show 8 items per page
    page_number = request.GET.get('page')
    feedback_data = paginator.get_page(page_number)
    context = {
        'feedback_data': feedback_data,
        'staff_data': statf_data,
        'search_form': search_form
    }
    return render(request, 'feedback/feedback_table.html', context)


@login_required(login_url='loginpage')
def overviewfeedback(request, pk):
    statf_data = StaffDetails.objects.get(username=request.user)
    contact_data = Feedback.objects.get(id=pk)
    context = {
        'contact_data': contact_data,
        'staff_data': statf_data
    }
    return render(request, 'feedback/feedback_overview.html', context)


@login_required(login_url='loginpage')
def deletefeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)
    feedback.delete()
    return redirect('allfeedback')


@login_required(login_url='loginpage')
def statusfeedback(request, pk):
    if request.user.is_staff:
        feedback = Feedback.objects.get(id=pk)

        feedback.status = not feedback.status

        # Save the changes to the database
        feedback.save()
        messages.success(request, "Satus updated successfully")
    else:
        messages.error(request, "You Don't have access")

    return redirect('allfeedback')

# End Feedbac Details Functions


# Charts Section


def chartjs(request):
    return render(request, 'charts/charts-chartjs.html')


def echarts(request):
    return render(request, 'charts/charts-echarts.html')


def apexcharts(request):
    return render(request, 'charts/charts-apexcharts.html')


def datatable(request):
    return render(request, 'tables/tables-data.html')


def generaltable(request):
    return render(request, 'tables/tables-general.html')


def contactpage(request):
    return render(request, 'pages/pages-contact.html')


def blankpage(request):
    return render(request, 'pages/pages-blank.html')


def error404page(request):
    return render(request, 'pages/pages-error-404.html')


def faqpage(request):
    return render(request, 'pages/pages-faq.html')


# Travel Agent Views

# Create your views here.


# def loginPage(request):
#     page = 'login'

#     # Redirect to 'company' if user is already authenticated
#     if request.user.is_authenticated:
#         return redirect('company')

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Check if the username exists in the database
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             messages.error(request, 'User does not exist')
#             return render(request, 'cmsapp/loginpage.html', {'page': page})

#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication was successful
#         if user is not None:
#             login(request, user)
#             return redirect('company')
#         else:
#             messages.error(request, 'Username or password is incorrect')
#             return render(request, 'cmsapp/loginpage.html', {'page': page})

#     context = {'page': page}
#     # If GET request or form submission failed, render the login page
#     return render(request, 'cmsapp/loginpage.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('login-page')


# def registerPage(request):
#     form = MyUserCreationForm()
#     context = {'form': form}

#     if request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, "An error occured during registeration!!")

#     return render(request, 'base/login_register.html', context)

# @login_required(login_url='login-page')
# def company(request):
#     form = CompanyForm()
#     userdata = StaffDetails.objects.get(username=request.user)
#     if request.method == 'POST':
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('company')

#     queryset = CompanyTable.objects.all()
#     paginator = Paginator(queryset, 8)  # Show 10 items per page

#     page_number = request.GET.get('page')
#     companydata = paginator.get_page(page_number)
#     contaxt = {
#         'compdata': companydata,
#         'form': form,
#         'userdata': userdata,
#         'name': request.user.username,
#     }
#     return render(request, 'cmsapp/addeditcompany.html', contaxt)


# # @login_required(login_url='login-page')
# def contact(request):
#     form = ContactForm()
#     search_form = ContactSearchForm(request.GET or None)
#     userdata = StaffDetails.objects.get(username=request.user)

#     if request.method == 'POST' and 'query' not in request.POST:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')

#     queryset = ContactTable.objects.all()

#     if search_form.is_valid():
#         query = search_form.cleaned_data.get('query')
#         start_date = search_form.cleaned_data.get('start_date')
#         end_date = search_form.cleaned_data.get('end_date')
#         if query:
#             queryset = queryset.filter(
#                 Q(person_name__icontains=query) |
#                 Q(person_email__icontains=query) |
#                 Q(person_phone__icontains=query) |
#                 Q(company_name__company_name__icontains=query)
#             )
#         if start_date and end_date:
#             queryset = queryset.filter(
#                 updated__date__range=(start_date, end_date)
#             )

#     paginator = Paginator(queryset, 8)  # Show 8 items per page
#     page_number = request.GET.get('page')
#     companydata = paginator.get_page(page_number)

#     context = {
#         'contdata': companydata,
#         'form': form,
#         'search_form': search_form,
#         'userdata': userdata
#     }

#     return render(request, 'cmsapp/addeditcontact.html', context)

#     # form = ContactForm()
#     # userdata = StaffDetails.objects.get(username=request.user)
#     # if request.method == 'POST':
#     #     form = ContactForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('contact')

#     # queryset = ContactTable.objects.all()
#     # paginator = Paginator(queryset, 8)  # Show 10 items per page

#     # page_number = request.GET.get('page')
#     # companydata = paginator.get_page(page_number)
#     # contaxt = {
#     #     'contdata': companydata,
#     #     'form': form,
#     #     'userdata': userdata
#     # }
#     # return render(request, 'cmsapp/addeditcontact.html', contaxt)


# # @login_required(login_url='login-page')
# def editcompany(request, pk):
#     userdata = StaffDetails.objects.get(username=request.user)
#     company = CompanyTable.objects.get(id=pk)
#     if request.method == "POST":
#         # Process the form submission with the existing company instance
#         form = CompanyForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()  # Save the updated instance
#             return redirect('company')
#     else:
#         form = CompanyForm(instance=company)

#     companydata = CompanyTable.objects.all()

#     contaxt = {
#         'compdata': companydata,
#         'form': form,
#         'userdata': userdata,
#     }
#     return render(request, 'cmsapp/addeditcompany.html', contaxt)


# # @login_required(login_url='login-page')
# def editcontact(request, pk):
#     userdata = StaffDetails.objects.get(username=request.user)
#     company = ContactTable.objects.get(id=pk)
#     if request.method == "POST":
#         # Process the form submission with the existing company instance
#         form = ContactForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()  # Save the updated instance
#             return redirect('contact')
#     else:
#         form = ContactForm(instance=company)
#     conatctdata = ContactTable.objects.all()

#     contaxt = {
#         'contdata': conatctdata,
#         'form': form,
#         'userdata': userdata
#     }
#     return render(request, 'cmsapp/addeditcontact.html', contaxt)


# # Delete Function for Company Table

# def deletecompany(request, pk):
#     company = CompanyTable.objects.get(id=pk)
#     company.delete()
#     return redirect('company')

# # Delete Function for Contact Table


# def deletecontact(request, pk):
#     company = ContactTable.objects.get(id=pk)
#     company.delete()
#     return redirect('contact')


# # def arivalhome(request):
# #     form = ArivalForm()
# #     context = {'form': form}
# #     return render(request, 'cmsapp/homeArival.html', context)

# # @login_required(login_url='login-page')
# def arivalform(request):
#     form = ArivalForm()
#     userdata = StaffDetails.objects.get(username=request.user)
#     if request.method == 'POST':
#         form = ArivalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('arivalform')

#     queryset = ArivalTable.objects.all()
#     paginator = Paginator(queryset, 8)  # Show 10 items per page

#     page_number = request.GET.get('page')
#     arivaldata = paginator.get_page(page_number)
#     context = {
#         'form': form,
#         'arivaldata': arivaldata,
#         'userdata': userdata}
#     return render(request, 'cmsapp/addeditArival.html', context)


# def deleteArival(request, pk):
#     company = ArivalTable.objects.get(id=pk)
#     company.delete()
#     return redirect('arivalform')


# # @login_required(login_url='login-page')
# def editarival(request, pk):
#     userdata = StaffDetails.objects.get(username=request.user)
#     company = ArivalTable.objects.get(id=pk)
#     if request.method == "POST":
#         # Process the form submission with the existing company instance
#         form = ArivalForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()  # Save the updated instance
#             return redirect('arivalform')
#     else:
#         form = ArivalForm(instance=company)
#     arivaldata = ArivalTable.objects.all()

#     contaxt = {
#         'arivaldata': arivaldata,
#         'form': form,
#         'userdata': userdata,
#     }
#     return render(request, 'cmsapp/addeditArival.html', contaxt)


# def loginview(request):
#     return render(request, 'cmsapp/loginpage.html')


# # @login_required(login_url='login-page')
# def datatableview(request):
#     # data = ContactTable.objects.all().values()
#     contacts = ContactTable.objects.all().select_related('company_name')
#     userdata = StaffDetails.objects.get(username=request.user)
#     data = [{
#         'id': contact.id,
#         'person_name': contact.person_name,  # or other contact fields
#         'person_city': contact.person_city,  # or other contact fields
#         'person_phone': contact.person_phone,  # or other contact fields
#         'person_email': contact.person_email,  # or other contact fields
#         'created': contact.created,  # or other contact fields
#         'updated': contact.updated,  # or other contact fields
#         # Access company name through the relation
#         'company_name': contact.company_name.company_name
#     } for contact in contacts]
#     # print(data)
#     return render(request, "datatable/datatable.html", {'data': data, 'userdata': userdata})


# def datatableview2(request):
#     return render(request, "datatable/datatable2.html")
