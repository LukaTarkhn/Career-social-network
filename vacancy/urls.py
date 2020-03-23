from django.urls import path

from . import views

urlpatterns = [
    path('vacancy', views.vacancy, name='vacancy')
]
