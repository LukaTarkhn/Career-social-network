from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model, authenticate
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
            return redirect('vacancy')
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
            return redirect('vacancy')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('vacancy')
        else:
            return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('vacancy')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
