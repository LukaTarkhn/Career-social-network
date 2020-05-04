from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model, authenticate
from django.core.paginator import Paginator

from accounts.models import Account, Specialization, Contact, WorkExperience, Education, Language, MoreEducation
from .forms import PersonalEditForm, EmailUrlEditForm, SpecializationEditForm, SpecializationAddForm, ContactAddForm, \
    ContactEditForm, WorkExperienceAddForm, WorkExperienceEditForm, EducationAddForm, EducationEditForm, \
    MoreEducationAddForm, MoreEducationEditForm, LanguageAddForm, LanguageEditForm
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
                    # add specialization section
                    specialization = SpecializationAddForm(request.POST or None)
                    contact = ContactAddForm(request.POST or None)
                    obj1 = specialization.save(commit=False)
                    obj1.user = Account.objects.get(email=email)
                    obj1.save()
                    obj2 = contact.save(commit=False)
                    obj2.user = Account.objects.get(email=email)
                    obj2.save()
                    # end specialization adding
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


def profile_edit(request):
    if request.user.is_authenticated:
        form = PersonalEditForm(request.POST or None, request.FILES or None, instance=request.user)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Personal information updated')
                return redirect('profile_edit')
        context = {'form': form}
        for field in form:
            for error in field.errors:
                messages.error(request, error)
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
                messages.success(request, 'Email and url updated')
        else:
            form = EmailUrlEditForm(
                initial={
                    'email': request.user.email,
                    'username': request.user.username,
                }
            )
        for field in form:
            for error in field.errors:
                messages.error(request, error)
        context['account_form'] = form
        return render(request, 'accounts/change_password.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def specialization_edit(request):
    if request.user.is_authenticated:
        owner = get_object_or_404(Specialization, user=request.user)
        form = SpecializationEditForm(request.POST or None, instance=owner)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Specialization information updated')
                return redirect('specialization_edit')
        context = {
            'form': form
        }
        return render(request, 'accounts/specialization_edit.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def contact_edit(request):
    if request.user.is_authenticated:
        owner = get_object_or_404(Contact, user=request.user)
        form = ContactEditForm(request.POST or None, instance=owner)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Contact information updated')
                return redirect('contact_edit')
        context = {
            'form': form
        }
        return render(request, 'accounts/contact_edit.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def experience(request):
    if request.user.is_authenticated:
        user_experience = WorkExperience.objects.filter(user=request.user).order_by('-date_created')

        paginator = Paginator(user_experience, 5)

        page_number = request.GET.get('p')
        page_obj = paginator.get_page(page_number)
        return render(request, 'accounts/experience/user_experience.html', {'page_obj': page_obj})
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def education(request):
    if request.user.is_authenticated:
        user_educations = Education.objects.filter(user=request.user).order_by('-date_created')
        user_languages = Language.objects.filter(user=request.user).order_by('-date_created')
        user_more_educations = MoreEducation.objects.filter(user=request.user).order_by('-date_created')

        educationP = Paginator(user_educations, 5)
        more_educationP = Paginator(user_more_educations, 5)
        languageP = Paginator(user_languages, 5)

        page_number = request.GET.get('p')
        educations = educationP.get_page(page_number)
        languages = languageP.get_page(page_number)
        more_educations = more_educationP.get_page(page_number)

        context = {
            'educations': educations,
            'languages': languages,
            'more_educations': more_educations
        }
        return render(request, 'accounts/education/user_education.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def experience_add(request):
    if request.user.is_authenticated:
        form = WorkExperienceAddForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Work experience added')
                return redirect('experience')
        context = {
            'form': form
        }
        for field in form:
            for error in field.errors:
                messages.error(request, error)
        return render(request, 'accounts/experience/experience_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def experience_edit(request, pk):
    if request.user.is_authenticated:
        experience_info = get_object_or_404(WorkExperience, pk=pk)
        if experience_info.user == request.user:
            form = WorkExperienceEditForm(request.POST or None, instance=experience_info)
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Experience information updated')
                    return redirect('experience')
            context = {'form': form}
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            return render(request, 'accounts/experience/experience_edit.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def experience_delete(request, pk):
    if request.user.is_authenticated:
        experience_info = get_object_or_404(WorkExperience, pk=pk)
        if experience_info.user == request.user:
            if request.method == 'POST':
                experience_info.delete()
                messages.success(request, 'Successfully deleted')
                return redirect('experience')
            context = {'experience_info': experience_info}
            return render(request, 'accounts/experience/experience_delete.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def education_add(request):
    if request.user.is_authenticated:
        form = EducationAddForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Education added')
                return redirect('education')
        context = {
            'form': form
        }
        return render(request, 'accounts/education/education_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def education_edit(request, pk):
    if request.user.is_authenticated:
        education_info = get_object_or_404(Education, pk=pk)
        if education_info.user == request.user:
            form = EducationEditForm(request.POST or None, instance=education_info)
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Education information updated')
                    return redirect('education')
            context = {'form': form}
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            return render(request, 'accounts/education/education_edit.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def education_delete(request, pk):
    if request.user.is_authenticated:
        education_info = get_object_or_404(Education, pk=pk)
        if education_info.user == request.user:
            if request.method == 'POST':
                education_info.delete()
                messages.success(request, 'Successfully deleted')
                return redirect('education')
            context = {'education_info': education_info}
            return render(request, 'accounts/education/education_delete.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def more_education_add(request):
    if request.user.is_authenticated:
        form = MoreEducationAddForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Education added')
                return redirect('education')
        context = {
            'form': form
        }
        for field in form:
            for error in field.errors:
                messages.error(request, error)
        return render(request, 'accounts/education_more/education_more_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def more_education_edit(request, pk):
    if request.user.is_authenticated:
        more_education_info = get_object_or_404(MoreEducation, pk=pk)
        if more_education_info.user == request.user:
            form = MoreEducationEditForm(request.POST or None, instance=more_education_info)
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Education information updated')
                    return redirect('education')
            context = {'form': form}
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            return render(request, 'accounts/education_more/education_more_edit.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def more_education_delete(request, pk):
    if request.user.is_authenticated:
        more_education_info = get_object_or_404(MoreEducation, pk=pk)
        if more_education_info.user == request.user:
            if request.method == 'POST':
                more_education_info.delete()
                messages.success(request, 'Successfully deleted')
                return redirect('education')
            context = {'more_education_info': more_education_info}
            return render(request, 'accounts/education_more/education_more_delete.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def language_add(request):
    if request.user.is_authenticated:
        form = LanguageAddForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Language added')
                return redirect('education')
        context = {
            'form': form
        }
        for field in form:
            for error in field.errors:
                messages.error(request, error)
        return render(request, 'accounts/language/language_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def language_edit(request, pk):
    if request.user.is_authenticated:
        language_info = get_object_or_404(Language, pk=pk)
        if language_info.user == request.user:
            form = LanguageEditForm(request.POST or None, instance=language_info)
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Language information updated')
                    return redirect('education')
            context = {'form': form}
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            return render(request, 'accounts/language/language_edit.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def language_delete(request, pk):
    if request.user.is_authenticated:
        language_info = get_object_or_404(Language, pk=pk)
        if language_info.user == request.user:
            if request.method == 'POST':
                language_info.delete()
                messages.success(request, 'Successfully deleted')
                return redirect('education')
            context = {'language_info': language_info}
            return render(request, 'accounts/language/language_delete.html', context)
        else:
            messages.success(request, 'This is not your account')
            return redirect('profile')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')
