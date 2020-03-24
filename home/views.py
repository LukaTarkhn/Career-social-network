from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('vacancies')
    else:
        return render(request, 'home/index.html')
