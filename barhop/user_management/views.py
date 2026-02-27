from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationFormStep1, RegistrationFormStep2, ProfileUpdateForm
from .models import Profile

@login_required
def update_profile(request):
    user = request.user # This is your Profile instance
    
    if request.method == 'POST':
        # 1. Check for 'Edit Profile' submission
        if 'edit_profile' in request.POST:
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.bio = request.POST.get('bio')
            user.save()
            messages.success(request, "Display info updated!")

        # 2. Check for 'Personal Info' submission
        elif 'personal_info' in request.POST:
            user.email = request.POST.get('email')
            user.date_of_birth = request.POST.get('date_of_birth')
            user.save()
            messages.success(request, "Personal details updated!")

        # 3. Check for 'Change Password' submission
        elif 'change_password' in request.POST:
            new_password = request.POST.get('password')
            if new_password:
                user.set_password(new_password) # Hashes the password properly
                user.save()
                # Important: keep the user logged in after password change
                update_session_auth_hash(request, user) 
                messages.success(request, "Password changed successfully!")

        return redirect('user_management:update_profile') # Refresh the page to show new data
        
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, "registration/update_profile.html", {'form': form})


def check_existing_username(request):
    username = request.GET.get("username")
    user = Profile.objects.filter(username=username)
    if user:
        return HttpResponse(status=200)
    return HttpResponse(status=404)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('bars:bar-list')

    if request.GET.get('reset') == '1':
        saved_email = request.session.get('registration_data', {}).get('email', '')
        request.session.pop('registration_data', None)
        request.session['back_email'] = saved_email
        return redirect('user_management:register')

    # Pick up saved email if coming from back button
    back_email = request.session.pop('back_email', '')

    # Get existing step 1 data from session
    reg_data = request.session.get('registration_data')

    if request.method == 'POST':
        if reg_data:
            form = RegistrationFormStep2(request.POST)
            print("Step 2 POST received")
            print("Form valid:", form.is_valid())
            print("Form errors:", form.errors)
            if form.is_valid():
                print("Creating user...")
                user = Profile.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=reg_data['email'],
                    password=reg_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    date_of_birth=form.cleaned_data['date_of_birth'],
                    user_type=form.cleaned_data['user_type'] or Profile.UserType.BARHOPPER,
                )
                print("User created:", user)
                login(request, user, backend='user_management.backends.EmailBackend')
                request.session.pop('registration_data', None)
                print("Redirecting to bar-list")
                return redirect('bars:bar-list')
        else:
            form = RegistrationFormStep1(request.POST)
            if form.is_valid():
                request.session['registration_data'] = {
                    'email': form.cleaned_data['email'],
                    'password': form.cleaned_data['password_1'],
                }
                request.session.modified = True
                return redirect('user_management:register')
    else:
        form = RegistrationFormStep2() if reg_data else RegistrationFormStep1(initial={'email': back_email} if back_email else None)

    return render(request, 'registration/register.html', {
        'form': form,
        'step': 2 if reg_data else 1,
    })

