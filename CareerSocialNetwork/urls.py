from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('', include('vacancy.urls')),
    path('', include('members.urls')),
    path('', include('organizations.urls')),
    path('users/', include('accounts.urls')),
    path('admin/', admin.site.urls), 
]
