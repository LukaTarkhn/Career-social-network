from django.urls import path

from . import views

urlpatterns = [
    path('organizations', views.organizations, name='organizations'),
    path('user/organizations', views.user_organizations, name='user_organizations'),
    path('organization/create', views.organization_add, name='organization_add'),
    path('organization/<str:url>', views.organization, name='organization'),
    path('organization/<str:url>/edit', views.organization_edit, name='organization_edit'),
    path('organization/<str:url>/delete', views.organization_delete, name='organization_delete'),
]

