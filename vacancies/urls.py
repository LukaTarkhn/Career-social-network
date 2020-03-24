from django.urls import path

from . import views

urlpatterns = [
    path('vacancies', views.vacancies, name='vacancies')
]
