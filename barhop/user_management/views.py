from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationFormStep1, RegistrationFormStep2, ProfileUpdateForm
from .models import Profile


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('bars:bar-list')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "registration/update_profile.html", {'form': form})


def check_existing_username(request):
    username = request.GET.get("username")
    user = Profile.objects.filter(username=username)
    if user:
        return HttpResponse(status=200)
    return HttpResponse(status=404)


def register_view(request):
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


def user_login(request):
    return render(request, 'login.html')
