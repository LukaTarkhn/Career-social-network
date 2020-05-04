from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import OrganizationEditForm, OrganizationAddForm, OrganizationOwnerAddForm, OrganizationOwnerStatusChange
from organizations.models import Organization, OrganizationOwner
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
    return render(request, 'organizations/user_organizations.html', context)


def organization(request, url):
    organization_profile = get_object_or_404(Organization, url=url)
    if request.user.is_authenticated:
        owners = OrganizationOwner.objects.filter(user=request.user)
    else:
        owners = []

    context = {
        'organization_profile': organization_profile,
        'owners': owners
    }

    return render(request, 'organizations/organization.html', context)


def organization_add(request):
    if request.user.is_authenticated:
        form = OrganizationAddForm(request.POST or None)
        ownerForm = OrganizationOwnerAddForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                obj.url = secrets.token_hex(5) + str((int(time.time())))
                obj.save()
                owner = ownerForm.save(commit=False)
                owner.user = Account.objects.filter(email=request.user.email).first()
                owner.organization = Organization.objects.filter(pk=obj.id).first()
                owner.role = '2'
                owner.save()
                messages.success(request, 'Organization created')
                return redirect('organization', obj.url)
        context = {
            'form': form,
            'ownerForm': ownerForm
        }
        for field in form:
            for error in field.errors:
                messages.error(request, error)
        return render(request, 'organizations/organization_add.html', context)
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def organization_edit(request, url):
    if request.user.is_authenticated:
        organization_profile = get_object_or_404(Organization, url=url)
        owner = OrganizationOwner.objects.filter(organization=organization_profile.id,
                                                 user=request.user, role='2').exists()
        if owner:
            form = OrganizationEditForm(instance=organization_profile)
            if request.method == 'POST':
                form = OrganizationEditForm(request.POST or None, request.FILES or None, instance=organization_profile)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Personal information updated')
                    return redirect('organization_edit', organization_profile.url)
            context = {'form': form}
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
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
        owner = OrganizationOwner.objects.filter(organization=organization_for_delete.id,
                                                 user=request.user, role='2').exists()
        if owner:
            if request.method == 'POST':
                organization_for_delete.delete()
                messages.success(request, 'Organization successfully deleted')
                return redirect('user_organizations')
            context = {'organization_for_delete': organization_for_delete}
            return render(request, 'organizations/organization_delete.html', context)
        else:
            messages.success(request, 'This is not your organization')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def organization_admin(request, url):
    if request.user.is_authenticated:
        actualOrganization = get_object_or_404(Organization, url=url)
        owner = OrganizationOwner.objects.filter(organization=actualOrganization.id,
                                                 user=request.user, role='2').exists()
        users = Account.objects.all()
        owners = OrganizationOwner.objects.filter(organization=actualOrganization.id)
        ownersReversed = list(reversed(owners))

        ownerForm = OrganizationOwnerAddForm(request.POST or None)
        if owner:
            if not False:
                if request.method == 'POST':
                    exists = OrganizationOwner.objects.filter(organization=actualOrganization.id,
                                                              user=users.get(email=request.POST['user'])).exists()
                    if not exists:
                        if ownerForm.is_valid():
                            owner = ownerForm.save(commit=False)
                            owner.user = users.get(email=request.POST['user'])
                            owner.organization = actualOrganization
                            owner.save()
                            messages.success(request, 'Admin added')
                            return redirect('organization_admin', actualOrganization.url)
                    else:
                        messages.error(request, 'User is already added as admin')
                        return redirect('organization_admin', actualOrganization.url)
                context = {
                    'ownerForm': ownerForm,
                    'users': users,
                    'actualOrganization': actualOrganization,
                    'owners': ownersReversed
                }
                return render(request, 'organizations/organization_admin.html', context)
        else:
            messages.success(request, 'This is not your organization')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def organization_admin_delete(request, url):
    if request.user.is_authenticated:
        actualOrganization = get_object_or_404(Organization, url=url)

        administrator = OrganizationOwner.objects.filter(organization=actualOrganization.id,
                                                         user=request.user, role='2').exists()
        users = Account.objects.all()
        admin = OrganizationOwner.objects.filter(organization=actualOrganization.id,
                                                 user=users.get(email=request.POST['user']))

        if administrator:
            if request.method == 'POST':
                admin.delete()
                messages.success(request, 'Admin Deleted')
                return redirect('organization_admin', actualOrganization.url)
            context = {'organization_for_delete': actualOrganization}
            return render(request, 'organizations/organization_delete.html', context)
        else:
            messages.success(request, 'This is not your organization')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')


def organization_admin_status_change(request, url):
    if request.user.is_authenticated:
        organization_profile = get_object_or_404(Organization, url=url)
        owner = OrganizationOwner.objects.filter(organization=organization_profile.id,
                                                 user=request.user, role='2').exists()
        users = Account.objects.all()
        admin = OrganizationOwner.objects.filter(organization=organization_profile.id,
                                                 user=users.get(email=request.POST['user'])).first()
        if owner:
            form = OrganizationOwnerStatusChange(request.POST, instance=admin)
            if request.method == 'POST':
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.save()
                    messages.success(request, 'Status Updated')
                    return redirect('organization_admin', organization_profile.url)
            context = {'form': form}
            return render(request, 'organizations/organization_edit.html', context)
        else:
            messages.success(request, 'This is not your organization')
            return redirect('organizations')
    else:
        messages.error(request, 'How about register first?')
        return redirect('register')
