from django.urls import path

from . import views

urlpatterns = [
    path('sign_in', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('sign_up', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]
