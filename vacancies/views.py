from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, F
from functools import reduce

from .forms import VacancyAddForm, VacancyEditForm, ResponseAddForm, ResponseEditForm
from vacancies.models import Vacancy, VacancyResponse
from organizations.models import OrganizationOwner, Organization
from accounts.models import Account

import secrets
import time
import operator
from django.utils.timezone import now


def is_valid_param(param):
    return param != '' and param is not None and param


def is_num(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


def vacancies(request):
    vacancy_info = Vacancy.objects.order_by('-date_created')
    Account.objects.filter(pk=request.user.pk).update(last_login=now())

    search = request.GET.get('search')
    sortBy = request.GET.get('sortBy')
    remote = request.GET.get('remote')
    with_salary = request.GET.get('with_salary')
    spheres = request.GET.getlist('sphere')
    qualifications = request.GET.getlist('qualification')
    types = request.GET.get('work_type')
    skills = request.GET.getlist('skills')
    SPHERES = Vacancy.SPHERE
    QUALIFICATIONS = Vacancy.QUALIFICATION
    TYPES = Vacancy.TYPE
    SKILLS = Vacancy.SKILL
    if is_valid_param(search) and not is_num(search):
        vacancy_info = vacancy_info.filter(Q(title__icontains=search) | Q(location__icontains=search)
                                           | Q(organization__organization_name__icontains=search))
    elif is_valid_param(search) and is_num(search):
        vacancy_info = vacancy_info.filter(salary__gte=search)
    if is_valid_param(sortBy):
        if sortBy == '2':
            vacancy_info = vacancy_info.order_by(F('salary').desc(nulls_last=True))
        elif sortBy == '3':
            vacancy_info = vacancy_info.order_by('salary')
        else:
            vacancy_info = vacancy_info.order_by('-date_created')
    if is_valid_param(spheres):
        vacancy_info = vacancy_info.filter(reduce(operator.or_, (Q(sphere__icontains=i) for i in spheres)))
    if is_valid_param(qualifications):
        vacancy_info = vacancy_info.filter(
            reduce(operator.or_, (Q(qualification__icontains=i) for i in qualifications))
        )
    if is_valid_param(types):
        vacancy_info = vacancy_info.filter(work_type=types)
    if is_valid_param(skills):
        vacancy_info = vacancy_info.filter(reduce(operator.or_, (Q(skills__icontains=i) for i in skills)))
    if is_valid_param(remote) and remote == 'on':
        vacancy_info = vacancy_info.filter(remote_work=True)
    if is_valid_param(with_salary) and with_salary == 'on':
        vacancy_info = vacancy_info.filter(salary__gte=0)

    paginator = Paginator(vacancy_info, 8)

    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'sortBy': sortBy,
        'remote': remote,
        'with_salary': with_salary,
        'spheres': spheres,
        'qualifications': qualifications,
        'types': types,
        'skills': skills,
        'SPHERES': SPHERES,
        'QUALIFICATIONS': QUALIFICATIONS,
        'TYPES': TYPES,
        'SKILLS': SKILLS,
    }
    return render(request, 'vacancies/vacancies.html', context)


def vacancies_by_organization(request, url):
    if request.user.is_authenticated:
        owner = OrganizationOwner.objects.filter(user=request.user, organization__url=url).exists()
        if owner:
            vacancy_info = Vacancy.objects.filter(organization__url=url).order_by('-date_created')
            paginator = Paginator(vacancy_info, 8)

            page_number = request.GET.get('p')
            page_obj = paginator.get_page(page_number)
            return render(request, 'vacancies/vacancies_by_organization.html', {'page_obj': page_obj})
        else:
            messages.error(request, 'You have not permissions to see this page')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def vacancy(request, url):
    vacancy_info = get_object_or_404(Vacancy, url=url)
    responses = VacancyResponse.objects.filter(vacancy__url=url)
    form = ResponseAddForm(request.POST or None)
    if request.user.is_authenticated:
        owner = OrganizationOwner.objects.filter(organization=vacancy_info.organization.id,
                                                 user=request.user).exists()
        response = responses.filter(user=request.user).first()
        if not response:
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.vacancy = vacancy_info
                    obj.user = request.user
                    obj.save()
                    messages.success(request, 'Response added')
                    return redirect('vacancy', vacancy_info.url)
    else:
        owner = []
        response = []

    context = {
        'vacancy_info': vacancy_info,
        'responses': responses,
        'response': response,
        'owner': owner,
        'form': form
    }

    return render(request, 'vacancies/vacancy.html', context)


def vacancies_add(request, url):
    if request.user.is_authenticated:
        owner = OrganizationOwner.objects.filter(user=request.user, organization__url=url).exists()
        form = VacancyAddForm(request.POST or None)
        if owner:
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.url = secrets.token_hex(5) + str((int(time.time())))
                    obj.organization = Organization.objects.filter(url=url).first()
                    obj.save()
                    messages.success(request, 'Vacancy added')
                    return redirect('vacancy', obj.url)
        else:
            messages.error(request, 'You have not permissions to see this page')
            return redirect('vacancies')
        context = {
            'form': form
        }
        for field in form:
            for error in field.errors:
                messages.error(request, error)
        return render(request, 'vacancies/vacancy_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def vacancies_add_modal(request):
    if request.user.is_authenticated:
        owners = OrganizationOwner.objects.filter(user=request.user)
        user_organization = []
        for owner in owners:
            user_organization += Organization.objects.filter(id=owner.organization.id)

        paginator = Paginator(list(reversed(user_organization)), 8)
        page_number = request.GET.get('p')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'owners': owners
        }
        return render(request, 'vacancies/vacancy_add_modal.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def vacancy_edit(request, url):
    if request.user.is_authenticated:
        vacancy_info = get_object_or_404(Vacancy, url=url)
        owner = OrganizationOwner.objects.filter(user=request.user,
                                                 organization__url=vacancy_info.organization.url).exists()
        if owner:
            form = VacancyEditForm(instance=vacancy_info)
            if request.method == 'POST':
                form = VacancyEditForm(request.POST or None, instance=vacancy_info)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Vacancy information updated')
                    return redirect('vacancy_edit', vacancy_info.url)
            context = {
                'form': form,
                'vacancy_info': vacancy_info,
            }
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            return render(request, 'vacancies/vacancy_edit.html', context)
        else:
            messages.success(request, 'You have not permissions to see this page')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def vacancy_delete(request, url):
    if request.user.is_authenticated:
        vacancy_for_delete = get_object_or_404(Vacancy, url=url)
        owner = OrganizationOwner.objects.filter(user=request.user,
                                                 organization__url=vacancy_for_delete.organization.url,
                                                 role='2').exists()
        if owner:
            if request.method == 'POST':
                vacancy_for_delete.delete()
                messages.success(request, 'Vacancy successfully deleted')
                return redirect('vacancies_by_organization', vacancy_for_delete.organization.url)
            context = {'vacancy_for_delete': vacancy_for_delete}
            return render(request, 'vacancies/vacancy_delete.html', context)
        else:
            messages.success(request, 'You have not permissions to see this page')
            return redirect('vacancies_by_organization', vacancy_for_delete.organization.url)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def user_responses(request):
    if request.user.is_authenticated:
        responses = VacancyResponse.objects.filter(user=request.user).order_by('-date_created')
        paginator = Paginator(responses, 8)

        page_number = request.GET.get('p')
        page_obj = paginator.get_page(page_number)

        context = {
            'responses': page_obj,
        }
        return render(request, 'vacancies/responses.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def response_delete(request, url):
    if request.user.is_authenticated:
        vacancy_info = get_object_or_404(Vacancy, url=url)
        response = VacancyResponse.objects.filter(vacancy__url=url, user=request.user).first()
        if request.method == 'POST':
            response.delete()
            messages.success(request, 'Response deleted')
            return redirect('vacancy', vacancy_info.url)
        context = {
            'response': response,
            'vacancy_info': vacancy_info
        }
        return render(request, 'vacancies/response_delete.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def response_status_change(request, url, user_id):
    if request.user.is_authenticated:
        response = get_object_or_404(VacancyResponse, vacancy__url=url, user=user_id)
        owner = OrganizationOwner.objects.filter(organization=response.vacancy.organization.id,
                                                 user=request.user).exists()
        if owner:
            if request.method == 'POST':
                status_change_form = ResponseEditForm(request.POST or None, instance=response)
                if status_change_form.is_valid():
                    obj = status_change_form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Status changed')
                    return redirect('vacancy', url)
        else:
            messages.success(request, 'You have not permissions to see this page')
            return redirect('vacancy', url)
        context = {
            'response': response
        }
        return render(request, 'vacancies/vacancy.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')
