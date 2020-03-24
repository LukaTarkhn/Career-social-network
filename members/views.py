from django.shortcuts import render
from django.core.paginator import Paginator

from accounts.models import Account


def members(request):
    accounts = Account.objects.order_by('-last_login')
    paginator = Paginator(accounts, 8)

    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    return render(request, 'members/members.html', {'page_obj': page_obj})
