from django.shortcuts import render


def vacancy(request):
    return render(request, 'vacancy/vacancy.html')
