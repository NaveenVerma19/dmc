from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from crm.models import StaffDetails
from crm.forms import StaffDetailsForm
import os
from datetime import datetime


# Create your views here.


# Need to work On it
def loginpage(request):
    page = 'loginpage'

    # Redirect to 'company' if user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists in the database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.info(request, 'User does not exist')
            return render(request, 'loginaccounts.html', {'page': page})

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            login(request, user)

            # Check if StaffDetails object exists for the authenticated user
            if StaffDetails.objects.filter(username=user).exists():
                # StaffDetails object exists, redirect to home page
                return redirect('profilepage')
            else:
                return redirect('addprofile')
            # redirect('profile_creation_view')
        else:
            messages.warning(request, 'Username or password is incorrect')
            return render(request, 'loginaccounts.html', {'page': page})

    context = {'page': page}
    # If GET request or form submission failed, render the login page

    return render(request, 'loginaccounts.html', context)


@login_required(login_url='loginpage')
def addprofile(request):
    user = request.user
    if StaffDetails.objects.filter(username=user).exists():
        return redirect('profilepage')
    else:
        if request.method == "POST":
            # Process the form submission with the existing company instance
            form = StaffDetailsForm(request.POST, request.FILES)
            if form.is_valid():
                user_details = form.save(commit=False)

                if request.FILES.get('avatar'):
                    profile_file = request.FILES['avatar']
                    ext_profile = profile_file.name.split('.')[-1]  # Get file extension
                    new_profile = f"{form.cleaned_data['user_full_name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext_profile}"
                    user_details.avatar.name = os.path.join('photos/', new_profile)

                user_details.username = request.user
                form.save()  # Save the updated instance
                return redirect('profilepage')
        else:
            form = StaffDetailsForm()

    context = {'form': form}
    return render(request, 'user_profile/profile_add.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginpage')


# Need to work On it

def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
        else:
            return HttpResponse("Something error in registring your accounts, Kindly contact to admin@chalodmc.com")
    context = {
        'form': form
    }
    return render(request, 'registeraccounts.html', context)
