from django.urls import path

from . import views

urlpatterns = [
    path('vacancies', views.vacancies, name='vacancies'),
    path('vacancy/<str:url>', views.vacancy, name='vacancy'),
    path('organization/<str:url>/vacancies', views.vacancies_by_organization, name='vacancies_by_organization'),
    path('vacancy/add/modal', views.vacancies_add_modal, name='vacancy_add_modal'),
    path('vacancy/<str:url>/edit', views.vacancy_edit, name='vacancy_edit'),
    path('vacancy/<str:url>/delete', views.vacancy_delete, name='vacancy_delete'),
    path('response/<str:url>/delete', views.response_delete, name='response_delete'),
    path('vacancy/<str:url>/response/<str:user_id>/edit', views.response_status_change, name='response_status_change'),
    path('organizations/<str:url>/vacancies/add', views.vacancies_add, name='vacancies_add'),
    path('personal/responses', views.user_responses, name='user_responses'),
]
