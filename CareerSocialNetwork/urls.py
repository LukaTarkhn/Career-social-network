from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', include('home.urls')),
    path('', include('vacancies.urls')),
    path('', include('members.urls')),
    path('', include('organizations.urls')),
    path('profile/', include('accounts.urls')),
    path('', include('organizations.urls')),
    path('', include('vacancies.urls')),
    path('', include('conversations.urls')),
    path('admin/', admin.site.urls),

    path('reset_password',
         auth_views.PasswordResetView.as_view
         (template_name='accounts/reset_password/reset_password.html',
          html_email_template_name='accounts/reset_password/reset_password_email.html'),
         name="reset_password"),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view
         (template_name='accounts/reset_password/reset_password_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view
         (template_name='accounts/reset_password/reset_password_confirm.html'),
         name="password_reset_confirm"),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view
         (template_name='accounts/reset_password/reset_password_complete.html'),
         name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
