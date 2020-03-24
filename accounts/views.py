from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model, authenticate

from accounts.models import Account
from .forms import PersonalEditForm, PasswordChangeForm
import secrets
import time

User = get_user_model()


def register(request):
    if request.method == 'POST':
        # Get form values
        username = secrets.token_hex(5) + str((int(time.time())))
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        # Check if password match
        if password == re_password:
            # Check email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email address already registered')
                return redirect('register')
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Chance of this error is 0.000000000000001%, congrats! reload page')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password
                    )
                    # auth.login(request, user)
                    # messages.success(request, 'You are now registered and authorized')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        if request.user.is_authenticated:
            return redirect('vacancies')
        else:
            return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email.lower(), password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('vacancies')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('vacancies')
        else:
            return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('vacancies')


def profile(request, username):
    user_profile = get_object_or_404(Account, username=username)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'accounts/profile.html', context)


def profile_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PersonalEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Personal information updated')
                return redirect('profile_edit')
            else:
                messages.error(request, 'This link already used')
                return redirect('profile_edit')
        return render(request, 'accounts/profile_edit.html')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Information updated')
                return redirect('change_password')
            else:
                messages.error(request, 'This email already used')
                return redirect('change_password')
        return render(request, 'accounts/change_password.html')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')
