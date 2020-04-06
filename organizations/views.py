from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import OrganizationEditForm, OrganizationAddForm
from organizations.models import Organization
from accounts.models import Account

import secrets
import time


def organizations(request):
    organizations_info = Organization.objects.order_by('-date_created')

    paginator = Paginator(organizations_info, 8)

    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    return render(request, 'organizations/organizations.html', {'page_obj': page_obj})


def user_organizations(request):
    user_organization = Organization.objects.filter(user=request.user)

    paginator = Paginator(user_organization, 8)

    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    return render(request, 'organizations/user_organizations.html', {'page_obj': page_obj})


def organization(request, url):
    organization_profile = get_object_or_404(Organization, url=url)
    context = {'organization_profile': organization_profile}

    return render(request, 'organizations/organization.html', context)


def organization_add(request):
    if request.user.is_authenticated:
        form = OrganizationAddForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = Account.objects.filter(email=request.user.email).first()
                obj.url = secrets.token_hex(5) + str((int(time.time())))
                obj.save()
                messages.success(request, 'Organization created')
                return redirect('organization', obj.url)
        context = {'form': form}
        return render(request, 'organizations/organization_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def organization_edit(request, url):
    if request.user.is_authenticated:
        organization_profile = get_object_or_404(Organization, url=url)
        if request.user == organization_profile.user:
            form = OrganizationEditForm(instance=organization_profile)
            if request.method == 'POST':
                form = OrganizationEditForm(request.POST or None, request.FILES or None, instance=organization_profile)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Personal information updated')
                    return redirect('organization_edit',  organization_profile.url)
            context = {'form': form}
            return render(request, 'organizations/organization_edit.html', context)
        else:
            messages.success(request, 'This is not your organization')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def organization_delete(request, url):
    if request.user.is_authenticated:
        organization_for_delete = get_object_or_404(Organization, url=url)
        if request.user == organization_for_delete.user:
            if request.method == 'POST':
                organization_for_delete.delete()
                return redirect('user_organizations')
            context = {'organization_for_delete': organization_for_delete}
            return render(request, 'organizations/organization_delete.html', context)
        else:
            messages.success(request, 'This is not your organization')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')