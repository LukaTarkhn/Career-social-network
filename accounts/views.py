from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model, authenticate

from accounts.models import Account
from .forms import PersonalEditForm, EmailUrlEditForm
import secrets
import time
from datetime import date

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
    Age = 0
    if user_profile.birth_day:
        today = date.today()
        Age = today.year - user_profile.birth_day.year - ((user_profile.birth_day.month, user_profile.birth_day.day) <
                                                          (user_profile.birth_day.month, user_profile.birth_day.day))
    context = {
        'user_profile': user_profile,
        'Age': Age
    }
    return render(request, 'accounts/profile.html', context)


# def profile_edit(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PersonalEditForm(request.POST, request.FILES, instance=request.user)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Personal information updated')
#                 return redirect('profile_edit')
#             else:
#                 messages.error(request, form.errors)
#                 return redirect('profile_edit')
#         return render(request, 'accounts/profile_edit.html')
#     else:
#         messages.error(request, 'How about register first?')
#         return redirect('register')


def profile_edit(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == 'POST':
            form = PersonalEditForm(request.POST or None,  request.FILES or None, instance=request.user)
            if form.is_valid():
                form.initial = {
                    'first_name': request.POST['first_name'],
                    'last_name': request.POST['last_name'],
                    'about_me': request.POST['about_me'],
                    'birth_day': request.POST['birth_day'],
                    'living_city': request.POST['living_city'],
                    'gender': request.POST['gender'],
                    'website': request.POST['website'],
                }
                form.save()
                messages.success(request, 'Personal information updated')
                return redirect('profile_edit')
        else:
            form = PersonalEditForm(
                initial={
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'about_me': request.user.about_me,
                    'birth_day': request.user.birth_day,
                    'living_city': request.user.living_city,
                    'gender': request.user.gender,
                    'website': request.user.website,
                    'profile_pic': request.user.profile_pic
                }
            )
        context['form'] = form
        return render(request, 'accounts/profile_edit.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user = authenticate(username=request.user, password=current_password)
            if user is not None:
                if new_password == confirm_password:
                    if len(new_password) > 6:
                        user.set_password(new_password)
                        user.save()
                        messages.success(request, 'Password updated, sign-in with new password')
                        return redirect('login')
                    else:
                        messages.error(request, "Password must be at least 7 characters")
                        return redirect('change_email_url')
                else:
                    messages.error(request, "Password confirmation doesn't match the password")
                    return redirect('change_email_url')
            else:
                messages.error(request, "Current password isn't valid")
                return redirect('change_email_url')

        return render(request, 'accounts/change_password.html')
    else:
        messages.error(request, "Please sign-in")
        return redirect('login')


def change_email_url(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == 'POST':
            form = EmailUrlEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.initial = {
                    'email': request.POST['email'],
                    'username': request.POST['username']
                }
                form.save()
                context['success_message'] = 'Email and url updated'
        else:
            form = EmailUrlEditForm(
                initial={
                    'email': request.user.email,
                    'username': request.user.username,
                }
            )
        context['account_form'] = form
        return render(request, 'accounts/change_password.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')

##### this 2 i can use in editing and adding organization
# def personal_info_edit(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         messages.error(request, "Please sign-in")
#         return redirect('login')
#     if request.method == 'POST':
#         form = PersonalMoreEditForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             person = Account.objects.filter(email=user.email).first()
#             obj.user = person
#             obj.save()
#
#         context['form'] = form
#     return render(request, 'accounts/profile_info_edit.html', context)

# def personal_info_edit(request, slug):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         messages.error(request, "Please sign-in")
#         return redirect('login')
#     personal_info = get_object_or_404(AccountMore, slug=slug)
#     if request.method == 'POST':
#         form = PersonalMoreEditForm(request.POST or None, request.FILES or None, instance=request.user)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             person = Account.objects.filter(email=user.email).first()
#             obj.user = person
#             personal_info = obj
#
#     form = PersonalMoreEditForm(
#         initial={
#             'profile_pic': personal_info.profile_pic,
#             'about_me': personal_info.about_me,
#             'birth_day': personal_info.birth_day,
#             'living_city': personal_info.living_city
#         }
#     )
#     context['form'] = form
#     return render(request, 'accounts/profile_info_edit.html', context)
