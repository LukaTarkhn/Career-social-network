from django.urls import path

from . import views

urlpatterns = [
    path('sign_in', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('sign_up', views.register, name='register'),
    path('personal/edit', views.profile_edit, name='profile_edit'),
    path('privacy/password', views.change_password, name='change_password'),
    path('privacy/edit', views.change_email_url, name='change_email_url'),
    path('<str:username>', views.profile, name='profile'),
]
