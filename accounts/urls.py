from django.urls import path

from . import views

urlpatterns = [
    path('sign_in', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('sign_up', views.register, name='register'),
    path('personal/edit', views.profile_edit, name='profile_edit'),
    path('privacy/password', views.change_password, name='change_password'),
    path('privacy/edit', views.change_email_url, name='change_email_url'),
    path('specialization/edit', views.specialization_edit, name='specialization_edit'),
    path('contact/edit', views.contact_edit, name='contact_edit'),
    path('experience', views.experience, name='experience'),
    path('education', views.education, name='education'),
    path('experience/create', views.experience_add, name='experience_add'),
    path('experience/<str:pk>/edit', views.experience_edit, name='experience_edit'),
    path('experience/<str:pk>/delete', views.experience_delete, name='experience_delete'),
    path('education/create', views.education_add, name='education_add'),
    path('education/<str:pk>/edit', views.education_edit, name='education_edit'),
    path('education/<str:pk>/delete', views.education_delete, name='education_delete'),
    path('more_education/create', views.more_education_add, name='more_education_add'),
    path('more_education/<str:pk>/edit', views.more_education_edit, name='more_education_edit'),
    path('more_education/<str:pk>/delete', views.more_education_delete, name='more_education_delete'),
    path('language/create', views.language_add, name='language_add'),
    path('language/<str:pk>/edit', views.language_edit, name='language_edit'),
    path('language/<str:pk>/delete', views.language_delete, name='language_delete'),
    path('<str:username>', views.profile, name='profile'),
]
