from django.urls import path

from . import views

urlpatterns = [
    path('sign_in', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('sign_up', views.register, name='register'),
    path('personal/edit', views.profile_edit, name='profile_edit'),
    path('personal/change_password', views.change_password, name='change_password'),
    path('<str:username>', views.profile, name='profile'),
]
