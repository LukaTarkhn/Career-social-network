from django.urls import path

from . import views

urlpatterns = [
    path('organizations', views.organizations, name='organizations'),
    path('organizations/mine', views.user_organizations, name='user_organizations'),
    path('organizations/create', views.organization_add, name='organization_add'),
    path('organizations/<str:url>', views.organization, name='organization'),
    path('organizations/<str:url>/edit', views.organization_edit, name='organization_edit'),
    path('organizations/<str:url>/delete', views.organization_delete, name='organization_delete'),
    path('organizations/<str:url>/admin_manage', views.organization_admin, name='organization_admin'),
    path('organizations/<str:url>/admin_delete', views.organization_admin_delete, name='organization_admin_delete'),
    path('organizations/<str:url>/status_change', views.organization_admin_status_change,
         name='organization_admin_status_change'),
]