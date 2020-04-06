from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.contrib.auth.models import Group


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone', 'living_city', 'gender', 'birth_day',
                    'profile_pic', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'username')
    search_fields = ('email', 'username', 'phone', 'first_name', 'last_name', 'living_city', 'gender', 'birth_day')
    list_editable = ('is_active',)
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

admin.site.unregister(Group)
