from django.shortcuts import render


def organizations(request):
    return render(request, 'organizations/organizations.html')
