"""
==============================================================================
ACCOUNTS VIEWS
Handles user registration, authentication, logout, and profile management.
==============================================================================
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

def register_view(request):
    """Handles new user creation and auto-profile generation."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome to Footprint Quest, {user.username}!")
            return redirect('dashboard:index')
        else:
            messages.error(request, "Please correct errors in the registration form.")
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    """Handles user sign in."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard:index')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """Signs out the user and redirects to landing page."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home:index')

@login_required
def profile_view(request):
    """Displays and updates user profile info."""
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})
