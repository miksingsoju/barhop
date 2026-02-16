from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProfileForm
from .models import Profile


@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProfileForm(instance=profile)
    return render(request, "update_profile.html", {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Profile for this user
            Profile.objects.create(
                user=user,
                first_name=user.username,  # default name, can be edited later,
                last_name=user.username,
                email=user.email if user.email else f"{user.username}@example.com",
            )

            login(request, user)
            return redirect('/')  # or your actual profile/homepage
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
